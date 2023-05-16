import asyncio


class EthernetDump:

    async def get_data(self, interface: str = 'wlp4s0', count_pkt: int = 1, type: str = 'ip', dns: bool = False) -> dict:
        process = await asyncio.create_subprocess_exec(
            'sudo', 'tcpdump', '-i', interface, '-n' if not dns else '', '-l', '-c', str(
                count_pkt), '-t', str(type),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        return {interface: [x for x in stdout.decode().split('\n') if x]}

    async def get_data_by_port(self, interface: str = "wlp4s0", count_pkt: int = 1, dns: bool = False, port: int = 443) -> dict:
        process = await asyncio.create_subprocess_exec(
            'sudo', 'tcpdump', '-i', interface, '-n' if not dns else '', '-l',
            '-c', str(count_pkt), 'port', str(port),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        return {interface: [x for x in stdout.decode().split('\n') if x]}

    async def get_data_by_host(self, interface: str = "wlp4s0", count_pkt: int = 1, type: str = 'ip', dns: bool = False, host: str = "localhost") -> dict:
        process = await asyncio.create_subprocess_exec(
            'sudo', 'tcpdump', '-i', interface, '-n' if not dns else '', '-l',
            '-c', str(count_pkt), '-t', type, 'host', host,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        return {interface: [x for x in stdout.decode().split('\n') if x]}

    async def get_data_by_host_and_port(self, interface: str = "wlp4s0", count_pkt: int = 1, type: str = 'ip', dns: bool = False, host: str = "localhost", port: int = 443) -> dict:
        process = await asyncio.create_subprocess_exec(
            'sudo', 'tcpdump', '-i', interface, '-n' if not dns else '', '-l',
            '-c', str(count_pkt), '-t', type, 'and host', host, 'and port', str(port),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        return {interface: [x for x in stdout.decode().split('\n') if x]}
