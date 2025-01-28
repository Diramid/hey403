import sys
import subprocess
import platform


def check_internet_connection(ip="8.8.8.8"):
    system_platform = platform.system()

    if system_platform == "Linux" or system_platform == "Darwin":
        try:
            response = subprocess.run(
                ["ping", "-c", "2", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )

            if response.returncode == 0:
                return True
            else:
                sys.exit(
                    "No internet connection. Please check your internet connection."
                )

        except Exception as e:
            sys.exit("Error occurred while checking internet connection.")
    elif system_platform == "Windows":
        try:
            response = subprocess.run(
                ["ping", "-n", "2", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )

            if response.returncode == 0:
                return True
            else:
                sys.exit(
                    "No internet connection. Please check your internet connection."
                )

        except Exception as e:
            sys.exit("Error occurred while checking internet connection.")
