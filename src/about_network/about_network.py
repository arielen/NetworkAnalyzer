import requests
import time
import psutil

from datetime import datetime


async def get_my_ip_addr() -> dict:
    try:
        response = requests.get('https://ident.me', timeout=5)
        response.raise_for_status()
        return {'external_ip': response.text.strip()}
    except (requests.exceptions.RequestException, ValueError):
        return {'error': 'Unable to retrieve external IP address'}


class Traffic:
    strg_unit_dict = {
        'B': 1, 'kB': 10**3, 'MB': 10**6,
        'GB': 10**9, 'TB': 10**12, 'PB': 10**15,
    }
    start_time = time.time()
    begin_time = datetime.now()

    def __init__(self, interface: str = 'wlp4s0') -> None:
        io_counters = psutil.net_io_counters()
        self.interface = interface
        self.bytes_sent = io_counters.bytes_sent
        self.bytes_recv = io_counters.bytes_recv

    async def get_traffic(self, strg_unit: str = 'B') -> dict:
        net_io_counters = psutil.net_io_counters(pernic=True)[self.interface]
        sent = self.bytes_sent - net_io_counters.bytes_sent
        recv = self.bytes_recv - net_io_counters.bytes_recv
        return {
            'bytes_sent': round(sent / self.strg_unit_dict.get(strg_unit, 1), 1),
            'bytes_recv': round(recv / self.strg_unit_dict.get(strg_unit, 1), 1),
            'begin_time': self.begin_time,
            'end_time': datetime.now()
        }

    async def get_interfaces() -> dict:
        """
        Get all network interfaces
        """
        return {'interfaces': list(psutil.net_if_addrs().keys())}
