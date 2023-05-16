import asyncio

from fastapi import APIRouter, Query

from .about_network import (
    Traffic,
    get_my_ip_addr
)


router = APIRouter(
    prefix="/about_network",
    tags=["About Network"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("/myip")
async def my_ip() -> dict:
    """
    Find out your IP address on the global network.
    If return error, check your internet connection.
    """
    return await get_my_ip_addr()


@router.get("/get_interfaces")
async def get_interfaces() -> dict:
    """
    Get all network interfaces.
    """
    return await Traffic.get_interfaces()


@router.get("/get_traffic")
async def get_traffic(
    interface: str = "wlp4s0",
    strg_unit: str = Query(
        "B", description="Storage unit (B, kB, MB, GB, TB, PB)"
    ),
) -> dict:
    """
    Returns the amount of downloaded and sent traffic on the selected interface.
    """
    traffic = Traffic(interface)
    if strg_unit in Traffic.strg_unit_dict:
        return await traffic.get_traffic(strg_unit)
    return {"error": "Invalid storage unit"}
