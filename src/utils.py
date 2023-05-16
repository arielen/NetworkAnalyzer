import asyncio
import re


async def get_ping_status(url: str, count: int) -> dict:
    clean_url = re.sub(r'https?://(?:www\.)?(.*?)(?:/.*)?$', r'\1', url)
    process = await asyncio.create_subprocess_exec(
        'ping', '-c', str(count), clean_url,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return {clean_url: [x for x in stdout.decode().split('\n') if x]}


async def get_json_tcpdump(interface: str = 'wlp4s0', count: int = 1, type: str = 'ip', dns: bool = False) -> dict:
    process = await asyncio.create_subprocess_exec(
        'sudo', 'tcpdump', '-i', interface, '-n' if dns else '', '-l', '-c', str(
            count), '-t', str(type),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return {interface: [x for x in stdout.decode().split('\n') if x]}
