from typing import Dict, Any

from fastapi import APIRouter, Query

from .about_network import (
    Traffic,
    get_my_ip_addr,
    get_interfaces as a_get_interfaces
)


router = APIRouter(
    prefix="/about_network",
    tags=["About Network"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("/myip")
async def my_ip() -> Dict[str, Any]:
    """
    Узнать свой IP-адрес в глобальной сети.
    Если возникнет ошибка, проверьте свое интернет-соединение.

    :return: Ваш IP-адрес в глобальной сети
    :rtype: dict
    """
    return await get_my_ip_addr()


@router.get("/get_interfaces")
async def get_interfaces() -> Dict[str, Any]:
    """
    Получить все сетевые интерфейсы.

    :return: Словарь, содержащий все сетевые интерфейсы
    :rtype: dict
    """
    return await a_get_interfaces()


@router.get("/get_traffic")
async def get_traffic(
    interface: str = Query(
        description="Название сетевого интерфейса, откуда получить трафик (по умолчанию: 'wlp4s0')",
        default="wlp4s0",
    ),
    strg_unit: str = Query(
        description="Единица хранения (B, kB, MB, GB, TB, PB) (по умолчанию: 'B')",
        default="B",
        regex=r"^(B|kB|MB|GB|TB|PB)",
    ),
) -> Dict[str, Any]:
    """
    Возвращает количество загруженного и отправленного трафика на выбранном интерфейсе.

    :param interface: Название сетевого интерфейса, откуда получить трафик (по умолчанию: 'wlp4s0')
    :type interface: str
    :param strg_unit: Единица хранения (B, kB, MB, GB, TB, PB) (по умолчанию: 'B')
    :type strg_unit: str

    :return: Словарь, содержащий количество загруженного и отправленного трафика
    :rtype: dict
    """
    traffic = Traffic(interface)
    if strg_unit in Traffic.strg_unit_dict:
        return await traffic.get_traffic(strg_unit)
    return {"error": "Недопустимая единица хранения"}
