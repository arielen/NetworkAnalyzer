import asyncio

from fastapi import APIRouter, Query
from .eth_dump import EthernetDump


router = APIRouter(
    prefix="/eth_dump",
    tags=["Ethernet Dump"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_eth_dump(
    interface: str = Query(
        "wlp4s0",
        description="Interface name"
    ),
        count_pkt: int = Query(
            1,
            description="Number of packets to dump"
    ),
        type: str = Query(
            "ip",
            description="Type of packets (tcp, udp, ip, vlan, wlan)"
    ),
        dns: bool = Query(
            False,
            description="Use DNS to resolve hostnames instead of IP addresses"
    ),
) -> dict:
    """
    Make a Ethernet traffic dump on a specified interface and return a dictionary with the results.
    """
    responce = await EthernetDump().get_data(interface, count_pkt, type, dns)
    return responce


@router.get("/port")
async def get_eth_dump_extended(
    interface: str = Query(
        "wlp4s0",
        description="Interface name"
    ),
    count_pkt: int = Query(
        1,
        description="Number of packets to dump"
    ),
    dns: bool = Query(
        False,
        description="Use DNS to resolve hostnames instead of IP addresses"
    ),
    port: int = Query(
        443,
        description="Port number"
    ),
) -> dict:
    """
    Make a Ethernet traffic dump on a specified interface and return a dictionary with the results.
    More extended version.
    """
    try:
        responce = await asyncio.wait_for(
            EthernetDump().get_data_by_port(
                interface, count_pkt, dns, port
            ),
            timeout=15
        )
    except asyncio.TimeoutError:
        return {interface: 'timeout'}
    return responce


@router.get("/host")
async def get_eth_dump_extended(
    interface: str = Query(
        "wlp4s0",
        description="Interface name"
    ),
    count_pkt: int = Query(
        1,
        description="Number of packets to dump"
    ),
    type: str = Query(
        "ip",
        description="Type of packets (tcp, udp, ip, vlan, wlan)"
    ),
    dns: bool = Query(
        False,
        description="Use DNS to resolve hostnames instead of IP addresses"
    ),
    host: str = Query(
        "localhost",
        description="Hostname or IP address"
    ),
) -> dict:
    """
    Make a Ethernet traffic dump on a specified interface and return a dictionary with the results.
    More extended version.
    """
    try:
        responce = await asyncio.wait_for(
            EthernetDump().get_data_by_host(
                interface, count_pkt, type, dns, host
            ),
            timeout=15
        )
    except asyncio.TimeoutError:
        return {interface: 'timeout'}
    return responce


@router.get("/host_and_port")
async def get_eth_dump_extended(
    interface: str = Query(
        "wlp4s0",
        description="Interface name"
    ),
    count_pkt: int = Query(
        1,
        description="Number of packets to dump"
    ),
    type: str = Query(
        "ip",
        description="Type of packets (tcp, udp, ip, vlan, wlan)"
    ),
    dns: bool = Query(
        False,
        description="Use DNS to resolve hostnames instead of IP addresses"
    ),
    host: str = Query(
        "localhost",
        description="Hostname or IP address"
    ),
    port: int = Query(
        443,
        description="Port number"
    ),
) -> dict:
    """
    Make a Ethernet traffic dump on a specified interface and return a dictionary with the results.
    More extended version.
    """
    try:
        responce = await asyncio.wait_for(
            EthernetDump().get_data_by_host_and_port(
                interface, count_pkt, type, dns, host, port),
            timeout=15
        )
    except asyncio.TimeoutError:
        return {interface: 'timeout'}
    return responce
