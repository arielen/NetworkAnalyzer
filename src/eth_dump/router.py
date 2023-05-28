import asyncio

from typing import Dict, Any

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
        description="Название интерфейса",
        default="wlp4s0",
    ),
    count_pkt: int = Query(
        description="Количество пакетов для дампа",
        default=1,
    ),
    type: str = Query(
        description="Тип пакетов. Пример: tcp, udp, ip, vlan, wlan",
        default="ip",
    ),
    dns: bool = Query(
        description="Использовать DNS для разрешения имен хостов вместо IP-адресов",
        default=False,
    ),
) -> Dict[str, Any]:
    """
    Сделать дамп Ethernet-трафика на указанном интерфейсе и вернуть словарь с результатами.

    :param interface: Название сетевого интерфейса, откуда получить трафик (по умолчанию: 'wlp4s0')
    :type interface: str
    :param count_pkt: Количество пакетов для дампа (по умолчанию: 1)
    :type count_pkt: int
    :param type: Тип пакетов (tcp, udp, ip, vlan, wlan) (по умолчанию: 'ip')
    :type type: str
    :param dns: Использовать DNS для разрешения имен хостов вместо IP-адресов (по умолчанию: False)
    :type dns: bool

    :return: Словарь, содержащий количество загруженного и отправленного трафика
    :rtype: dict
    """
    responce = await EthernetDump().get_data(interface, count_pkt, type, dns)
    return responce


@router.get("/port")
async def get_eth_dump_extended(
    interface: str = Query(
        description="Название сетевого интерфейса",
        default="wlp4s0",
    ),
    count_pkt: int = Query(
        description="Количество пакетов для дампа",
        default=1,
    ),
    dns: bool = Query(
        description="Использовать DNS для разрешения имен хостов вместо IP-адресов",
        default=False,
    ),
    port: int = Query(
        description="Номер порта для дампа",
        default=443,
    ),
) -> Dict[str, Any]:
    """
    Сделать дамп Ethernet-трафика на указанном интерфейсе и вернуть словарь с результатами.
    Более расширенная версия.

    :param interface: Название сетевого интерфейса, откуда получить трафик (по умолчанию: 'wlp4s0')
    :type interface: str
    :param count_pkt: Количество пакетов для дампа (по умолчанию: 1)
    :type count_pkt: int
    :param dns: Использовать DNS для разрешения имен хостов вместо IP-адресов (по умолчанию: False)
    :type dns: bool
    :param port: Номер порта (по умолчанию: 443)
    :type port: int

    :return: Словарь, содержащий количество загруженного и отправленного трафика
    :rtype: dict
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
        description="Название сетевого интерфейса",
        default="wlp4s0",
    ),
    count_pkt: int = Query(
        description="Количество пакетов для дампа",
        default=1,
    ),
    type: str = Query(
        description="Тип пакетов. Пример: tcp, udp, ip, vlan, wlan",
        default="ip",
    ),
    dns: bool = Query(
        description="Использовать DNS для разрешения имен хостов вместо IP-адресов",
        default=False,
    ),
    host: str = Query(
        description="Имя или IP-адрес для дампа",
        default="localhost",
    ),
) -> Dict[str, Any]:
    """
    Сделать дамп Ethernet-трафика на указанном интерфейсе и вернуть словарь с результатами.
    Более расширенная версия.

    :param interface: Название сетевого интерфейса, откуда получить трафик (по умолчанию: 'wlp4s0')
    :type interface: str
    :param count_pkt: Количество пакетов для дампа (по умолчанию: 1)
    :type count_pkt: int
    :param type: Тип пакетов. Пример: tcp, udp, ip, vlan, wlan
    :type type: str
    :param dns: Использовать DNS для разрешения имен хостов вместо IP-адресов (по умолчанию: False)
    :type dns: bool
    :param host: Имя или IP-адрес для дампа (по умолчанию: 'localhost')
    :type host: str

    :return: Словарь, содержащий количество загруженного и отправленного трафика
    :rtype: dict
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
        description="Название сетевого интерфейса",
        default="wlp4s0",
    ),
    count_pkt: int = Query(
        description="Количество пакетов для дампа",
        default=1,
    ),
    type: str = Query(
        description="Тип пакетов. Пример: tcp, udp, ip, vlan, wlan",
        default="ip",
    ),
    dns: bool = Query(
        description="Использовать DNS для разрешения имен хостов вместо IP-адресов",
        default=False,
    ),
    host: str = Query(
        description="Имя или IP-адрес для дампа",
        default="localhost",
    ),
    port: int = Query(
        description="Номер порта",
        default=443,
    ),
) -> Dict[str, Any]:
    """
    Сделать дамп Ethernet-трафика на указанном интерфейсе и вернуть словарь с результатами.
    Более расширенная версия.

    :param interface: Название сетевого интерфейса, откуда получить трафик (по умолчанию: 'wlp4s0')
    :type interface: str
    :param count_pkt: Количество пакетов для дампа (по умолчанию: 1)
    :type count_pkt: int
    :param type: Тип пакетов. Пример: tcp, udp, ip, vlan, wlan
    :type type: str
    :param dns: Использовать DNS для разрешения имен хостов вместо IP-адресов (по умолчанию: False)
    :type dns: bool
    :param host: Имя или IP-адрес для дампа (по умолчанию: 'localhost')
    :type host: str
    :param port: Номер порта (по умолчанию: 443)
    :type port: int

    :return: Словарь, содержащий количество загруженного и отправленного трафика
    :rtype: dict
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
