import subprocess
import platform


def check_internet_connection(
    ip: str = "8.8.8.8", retries: int = 3, timeout: int = 2
) -> bool:

    ping_options: dict[str, str] = {
        "Windows": "-n",
        "Linux": "-c",
        "Darwin": "-c",
    }

    system_platform = platform.system()
    ping_flag = ping_options.get(system_platform)

    if not ping_flag:
        print(f"Your platform is not supported : {system_platform}")
        return False

    for attempt in range(1, retries + 1):
        try:
            subprocess.run(
                ["ping", ping_flag, "2", "-w", str(timeout), ip],
                check=True,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            return True
        except subprocess.CalledProcessError:
            print(f"Connection failed. Retrying...({attempt}/3)")
            continue
    print("All attempts failed. Please check your connection.")
    return False
