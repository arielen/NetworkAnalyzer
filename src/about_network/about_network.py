import requests
import time
import psutil

from datetime import datetime
from typing import Dict, Any


async def get_interfaces() -> Dict[str, Any]:
    """
    Asynchronously retrieves a dictionary of network interfaces and their associated addresses.

    :return: A dictionary with a single key, 'interfaces', that maps to a list of strings representing the names of 
             network interfaces.
    :rtype: dict
    """
    return {'interfaces': list(psutil.net_if_addrs().keys())}


async def get_my_ip_addr() -> Dict[str, Any]:
    """
    Asynchronously retrieves the external IP address of the machine by making a GET request to https://ident.me.

    :return: 
        - A dictionary containing the external IP address under the key 'external_ip' if the request is successful.
        - A dictionary containing the error message under the key 'error' if the request fails due to an exception or invalid response.
    :rtype: dict
    """
    try:
        response = requests.get('https://ident.me', timeout=5)
        response.raise_for_status()
        return {'external_ip': response.text.strip()}
    except (requests.exceptions.RequestException, ValueError):
        return {'error': 'Unable to retrieve external IP address'}


class Traffic:
    """
    The Traffic class is designed to monitor the amount of sent and received traffic through a specified network interface.
    """
    strg_unit_dict = {
        'B': 1, 'kB': 10**3, 'MB': 10**6,
        'GB': 10**9, 'TB': 10**12, 'PB': 10**15,
    }
    start_time = time.time()
    begin_time = datetime.now()

    def __init__(self, interface: str = 'wlp4s0') -> None:
        """
        Initializes a new instance of the class with the specified network interface and retrieves the number of bytes sent and received through it.

        :param interface: The name of the network interface to use (default: 'wlp4s0')
        :type interface: str

        :return: None
        :rtype: None
        """
        io_counters = psutil.net_io_counters()
        self.interface = interface
        self.bytes_sent = io_counters.bytes_sent
        self.bytes_recv = io_counters.bytes_recv

    async def get_traffic(self, strg_unit: str = 'B') -> Dict[str, Any]:
        """
        Asynchronously gets the amount of traffic sent and received by the network interface monitored by the current instance.

        :param strg_unit: A string indicating the unit of measurement to use for the traffic amount (default: 'B')
        :type strg_unit: str

        :return: A dictionary containing the amount of bytes sent and received, the start time of the monitoring, and the end time of the monitoring.
        :rtype: dict
        """
        net_io_counters = psutil.net_io_counters(pernic=True)[self.interface]
        sent = self.bytes_sent - net_io_counters.bytes_sent
        recv = self.bytes_recv - net_io_counters.bytes_recv
        return {
            'bytes_sent': round(sent / self.strg_unit_dict.get(strg_unit, 1), 1),
            'bytes_recv': round(recv / self.strg_unit_dict.get(strg_unit, 1), 1),
            'begin_time': self.begin_time,
            'end_time': datetime.now()
        }
