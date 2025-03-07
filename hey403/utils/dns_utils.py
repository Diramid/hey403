import ctypes
import logging
import os
import platform
import subprocess
import sys
from typing import Optional, List

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


class DNSManager:

    def __init__(self):
        self.platform = platform.system()
        self.logger = logging.getLogger(__name__)

    def _check_admin(self):
        if self.platform == "Windows":
            if not ctypes.windll.shell32.IsUserAnAdmin():
                self.logger.error("Please run as Administrator!")
                sys.exit(1)
        elif self.platform == "Linux":
            if os.geteuid() != 0:
                self.logger.error("Please run with sudo!")
                sys.exit(1)

    def _run_command(self, command: List[str], error_message: str) -> bool:
        try:
            subprocess.run(command, check=True, text=True)
            return True
        except subprocess.CalledProcessError as e:
            self.logger.error(f"{error_message}: {e}")
            return False

    def get_current_dns(self) -> str:
        self._check_admin()

        if self.platform == "Windows":
            result = subprocess.check_output("ipconfig /all", shell=True, text=True)
            dns_lines = [line for line in result.splitlines() if "DNS Servers" in line]
            return dns_lines[0].split(":")[1].strip() if dns_lines else "Unknown"

        elif self.platform == "Linux":
            result = subprocess.check_output(
                ["nmcli", "device", "show"],
                text=True
            ).splitlines()
            res = [line[13:].strip() for line in result if line.startswith('IP4.DNS')]
            return res[0].strip() or "Unknown"

        elif self.platform == "Darwin":
            result = subprocess.check_output(
                ["networksetup", "-getdnsservers", "Wi-Fi"], text=True
            )
            return result.strip() or "Unknown"
        else:
            raise ValueError(f"Unsupported platform: {self.platform}")

    def configure_dns(
        self, preferred_dns: str, alternative_dns: Optional[str] = None
    ) -> None:
        self._check_admin()

        if self.platform == "Windows":
            interface = self._get_active_interface_windows()
            if not interface:
                self.logger.error("No active interface found!")
                sys.exit(1)
            self._run_command(
                [
                    "netsh",
                    "interface",
                    "ip",
                    "set",
                    "dns",
                    interface,
                    "static",
                    preferred_dns,
                    "primary",
                ],
                "Error setting primary DNS",
            )
            if alternative_dns:
                self._run_command(
                    [
                        "netsh",
                        "interface",
                        "ip",
                        "add",
                        "dns",
                        interface,
                        alternative_dns,
                        "index=2",
                    ],
                    "Error setting alternative DNS",
                )
            self.logger.info("DNS successfully set!")

        elif self.platform == "Linux":
            connection = self._get_active_connection_linux()
            if not connection:
                self.logger.error("No active network connections found.")
                sys.exit(1)
            dns_servers = (
                f"{preferred_dns} {alternative_dns}"
                if alternative_dns
                else preferred_dns
            )
            self._configure_dns_linux(connection, dns_servers)

        elif self.platform == "Darwin":
            connection_type = self._get_active_interface_mac()
            if not connection_type:
                self.logger.error("No active network interfaces found!")
                sys.exit(1)
            dns_servers = (
                f"{preferred_dns} {alternative_dns}"
                if alternative_dns
                else preferred_dns
            )
            self._run_command(
                ["networksetup", "-setdnsservers", connection_type, dns_servers],
                "Error setting DNS",
            )
            self.logger.info(f"DNS successfully set for {connection_type}!")
        else:
            raise ValueError(f"Unsupported platform: {self.platform}")

    def unset_dns(self) -> None:
        self._check_admin()

        if self.platform == "Windows":
            interface = self._get_active_interface_windows()
            if not interface:
                self.logger.error("No active interface found!")
                sys.exit(1)
            self._run_command(
                ["netsh", "interface", "ip", "set", "dns", interface, "dhcp"],
                "Error unsetting DNS",
            )
            self.logger.info("DNS successfully unset!")

        elif self.platform == "Linux":
            connection = self._get_active_connection_linux()
            if not connection:
                self.logger.error("No active network connections found.")
                sys.exit(1)
            self._run_command(
                ["nmcli", "connection", "modify", connection, "ipv4.dns", ""],
                f"Failed to unset DNS for {connection}",
            )
            self._run_command(
                [
                    "nmcli",
                    "connection",
                    "modify",
                    connection,
                    "ipv4.ignore-auto-dns",
                    "no",
                ],
                f"Failed to enable auto-DNS for {connection}",
            )
            self._run_command(
                ["systemctl", "restart", "NetworkManager"],
                "Failed to restart NetworkManager",
            )
            self.logger.info("DNS successfully unset!")

        elif self.platform == "Darwin":
            connection_type = self._get_active_interface_mac()
            if not connection_type:
                self.logger.error("No active network interfaces found!")
                sys.exit(1)
            self._run_command(
                ["networksetup", "-setdnsservers", connection_type, "empty"],
                "Error unsetting DNS",
            )
            self.logger.info(f"DNS successfully unset for {connection_type}!")
        else:
            raise ValueError(f"Unsupported platform: {self.platform}")

    def _get_active_interface_windows(self) -> Optional[str]:
        try:
            result = subprocess.check_output(
                ["netsh", "interface", "show", "interface"], text=True
            ).splitlines()
            active_interfaces = [
                line.split()[-1] for line in result if "Connected" in line
            ]
            return active_interfaces[0] if active_interfaces else None
        except Exception as e:
            self.logger.error(f"Failed to get active interfaces: {e}")
            return None

    def _get_active_connection_linux(self) -> Optional[str]:
        try:
            result = subprocess.check_output(
                ["nmcli", "-t", "-f", "NAME", "connection", "show", "--active"],
                text=True,
            ).splitlines()
            return result[0] if result else None
        except FileNotFoundError as e:
            self.logger.error(
                f"Failed to get active connections, dependency {e.filename} not installed"
            )
            return None
        except Exception as e:
            self.logger.error(f"Failed to get active connections: {e}")
            return None

    def _get_active_interface_mac(self) -> Optional[str]:
        for interface in ["Wi-Fi", "Ethernet"]:
            try:
                subprocess.check_output(
                    ["networksetup", "-getdnsservers", interface], text=True
                )
                return interface
            except subprocess.CalledProcessError:
                continue
        return None

    def _configure_dns_linux(self, connection: str, dns_servers: str) -> None:
        commands = [
            (
                ["nmcli", "connection", "modify", connection, "ipv4.dns", dns_servers],
                "Failed to set DNS",
            ),
            (
                [
                    "nmcli",
                    "connection",
                    "modify",
                    connection,
                    "ipv4.ignore-auto-dns",
                    "yes",
                ],
                "Failed to ignore auto-DNS",
            ),
            (
                ["systemctl", "restart", "NetworkManager"],
                "Failed to restart NetworkManager",
            ),
        ]
        for cmd, err_msg in commands:
            if not self._run_command(cmd, err_msg):
                raise RuntimeError(f"Failed to configure DNS: {err_msg}")
        self.logger.info(f"DNS successfully set for connection: {connection}!")


def get_status_code_from_request(ip: str) -> Optional[int]:
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    try:
        response = requests.get(url=f"https://{ip}", timeout=10, verify=False)
        return response.status_code
    except requests.exceptions.RequestException:
        return None
