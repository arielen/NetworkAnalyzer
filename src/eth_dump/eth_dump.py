import asyncio

from typing import Dict, List


class EthernetDump:
    """
    The EthernetDump class is designed to monitor the amount of sent and received traffic through a specified network interface.
    """

    async def get_data(self, interface: str = 'wlp4s0', count_pkt: int = 1, type: str = 'ip', dns: bool = False) -> Dict[str, List[str]]:
        """
        Asynchronously captures packets from a network interface using tcpdump and returns the parsed data in a dictionary.

        :param interface: The network interface to capture packets from (default: 'wlp4s0')
        :type interface: str
        :param count_pkt: The number of packets to capture (default: 1)
        :type count_pkt: int
        :param type: The type of packets to capture (default: 'ip')
        :type type: str
        :param dns: Whether or not to perform DNS resolution on captured packets (default: False)
        :type dns: bool

        :return: A dictionary containing the captured data in a list under the specified interface key.
        :rtype: dict
        """
        process = await asyncio.create_subprocess_exec(
            'sudo', 'tcpdump', '-i', interface, '-n' if not dns else '', '-l', '-c', str(
                count_pkt), '-t', str(type),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        return {interface: [x for x in stdout.decode().split('\n') if x]}

    async def get_data_by_port(self, interface: str = "wlp4s0", count_pkt: int = 1, dns: bool = False, port: int = 443) -> Dict[str, List[str]]:
        """
        Asynchronously captures packets from a network interface using tcpdump with 
        the specified port and returns the parsed data in a dictionary.

        :param interface: The network interface to capture packets from (default: 'wlp4s0')
        :type interface: str
        :param count_pkt: The number of packets to capture (default: 1)
        :type count_pkt: int
        :param dns: Whether or not to perform DNS resolution on captured packets (default: False)
        :type dns: bool
        :param port: The port to capture packets on (default: 443)
        :type port: int

        :return: A dictionary containing the captured data in a list under the specified interface key.
        :rtype: dict
        """
        process = await asyncio.create_subprocess_exec(
            'sudo', 'tcpdump', '-i', interface, '-n' if not dns else '', '-l',
            '-c', str(count_pkt), 'port', str(port),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        return {interface: [x for x in stdout.decode().split('\n') if x]}

    async def get_data_by_host(self, interface: str = "wlp4s0", count_pkt: int = 1, type: str = 'ip', dns: bool = False, host: str = "localhost") -> Dict[str, List[str]]:
        """
        Asynchronously captures packets from a network interface using tcpdump with 
        the specified host and returns the parsed data in a dictionary.

        :param interface: The network interface to capture packets from (default: 'wlp4s0')
        :type interface: str
        :param count_pkt: The number of packets to capture (default: 1)
        :type count_pkt: int
        :param type: The type of packets to capture (default: 'ip')
        :type type: str
        :param dns: Whether or not to perform DNS resolution on captured packets (default: False)
        :type dns: bool
        :param host: The host to capture packets on (default: 'localhost')
        :type host: str

        :return: A dictionary containing the captured data in a list under the specified interface key.
        :rtype: dict
        """
        process = await asyncio.create_subprocess_exec(
            'sudo', 'tcpdump', '-i', interface, '-n' if not dns else '', '-l',
            '-c', str(count_pkt), '-t', type, 'and host', host,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        return {interface: [x for x in stdout.decode().split('\n') if x]}

    async def get_data_by_host_and_port(self, interface: str = "wlp4s0", count_pkt: int = 1, type: str = 'ip', dns: bool = False, host: str = "localhost", port: int = 443) -> Dict[str, List[str]]:
        """
        Asynchronously captures packets from a network interface using tcpdump with
        the specified host and port and returns the parsed data in a dictionary.

        :param interface: The network interface to capture packets from (default: 'wlp4s0')
        :type interface: str
        :param count_pkt: The number of packets to capture (default: 1)
        :type count_pkt: int
        :param type: The type of packets to capture (default: 'ip')
        :type type: str
        :param dns: Whether or not to perform DNS resolution on captured packets (default: False)
        :type dns: bool
        :param host: The host to capture packets on (default: 'localhost')
        :type host: str
        :param port: The port to capture packets on (default: 443)
        :type port: int

        :return: A dictionary containing the captured data in a list under the specified interface key.
        :rtype: dict
        """
        process = await asyncio.create_subprocess_exec(
            'sudo', 'tcpdump', '-i', interface, '-n' if not dns else '', '-l',
            '-c', str(count_pkt), '-t', type, 'and host', host, 'and port', str(port),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        return {interface: [x for x in stdout.decode().split('\n') if x]}
