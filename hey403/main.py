import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

import typer
from rich.console import Console
from rich.progress import Progress

from hey403.network.dns_servers import DNS_SERVERS
from hey403.services.dns_resolver import (
    set_dns,
    test_dns,
    ensure_protocol,
    get_current_dns,
    unset_dns,
)
from hey403.utils.network_utils import check_internet_connection
from hey403.utils.table import create_table

APP_VERSION = "1.0.0"

app = typer.Typer()


@app.command()
def main(
        url: str = typer.Option(None, "--url", help="URL to test DNS resolution"),
        set_dns_flag: bool = typer.Option(False, "--set", help="Set the fastest DNS automatically"),
        current_dns: bool = typer.Option(False, "--current-dns", "-c", help="Display the current DNS"),
        unset: bool = typer.Option(False, "--unset", help="Unset the DNS settings"),
        version: bool = typer.Option(False, "--version", "-v", help="Display the application version"),
):
    """Handle DNS testing, configuration, and version display."""
    try:
        console = Console()

        if version:
            console.print(f"[bold cyan]version:[/bold cyan] {APP_VERSION}")
            sys.exit(0)

        check_internet_connection()

        table = create_table()
        dns_success_list = []

        if current_dns:
            current_dns_ip = get_current_dns()
            dns = [dns for dns in DNS_SERVERS if dns["preferred"] == current_dns_ip]
            if dns:
                console.print(
                    "[yellow]Current DNS[/yellow]: ",
                    f"[cyan]{dns[0]['name']}[/cyan] with IP {dns[0]['preferred']}",
                )
            else:
                console.print(
                    "[yellow]Current DNS[/yellow]: ",
                    f"[cyan]Custom DNS[/cyan] - {current_dns_ip} (not in DNS_SERVERS)",
                )
            sys.exit(0)

        elif unset:
            unset_dns()
            console.print("[green]DNS unset successfully[/green]")
            sys.exit(0)

        if not url:
            console.print(
                "[red]Error: URL is required when not using --current-dns, --unset, or --version[/red]"
            )
            sys.exit(1)

        url = ensure_protocol(url)

        with Progress(console=console) as progress:
            task = progress.add_task(
                "[cyan]Testing DNS servers...[/cyan]", total=len(DNS_SERVERS)
            )
            with ThreadPoolExecutor(max_workers=min(32, len(DNS_SERVERS))) as executor:
                futures = {
                    executor.submit(test_dns, dns, url): dns for dns in DNS_SERVERS
                }
                for future in as_completed(futures):
                    try:
                        (
                            dns_name,
                            preferred_dns,
                            alternative_dns,
                            status_message,
                            response_time_display,
                        ) = future.result()
                        table.add_row(
                            dns_name,
                            preferred_dns,
                            alternative_dns,
                            status_message,
                            response_time_display,
                        )
                        if set_dns_flag and status_message == "[green]Success[/green]":
                            dns_success_list.append(
                                [
                                    dns_name,
                                    preferred_dns,
                                    alternative_dns,
                                    response_time_display,
                                ]
                            )
                    except Exception as e:
                        console.print(f"[red]Error testing DNS: {e}[/red]")
                    progress.update(task, advance=1)

        # Set the fastest DNS if --set is provided
        if set_dns_flag and dns_success_list:
            min_entry = min(dns_success_list, key=lambda x: float(x[-1].strip(" ms")))
            set_dns(min_entry[1], min_entry[2])
            console.print(f'"{min_entry[0]}" DNS set successfully')

        # Display the results table
        console.print(table)

    except Exception as e:
        console.print(f"[red]An unexpected error occurred: {e}[/red]")
        sys.exit(1)


if __name__ == "__main__":
    app()
