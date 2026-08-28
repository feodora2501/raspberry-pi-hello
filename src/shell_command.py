import re
import subprocess


def get_device_ip():
    command_result = subprocess.run(
        ["ip", "a"],
        capture_output=True,
        text=True,
        check=True
    )

    output = command_result.stdout.strip()
    ip_list = re.findall("\\d+\\.\\d+\\.\\d+\\.\\d+", output)

    for ip in ip_list:
        if not ip.startswith("127") and not ip.endswith("255"):
            return ip