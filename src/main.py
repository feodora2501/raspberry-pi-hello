from shell_command import get_device_ip
from tg_api import send_message

ip = get_device_ip()

send_message(ip)