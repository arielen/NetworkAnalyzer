from typing import Dict, Any
from fastapi import FastAPI, Query

from eth_dump.router import router as router_eth_dump
from about_network.router import router as router_about_network

from utils import (
    get_ping_status
)

app = FastAPI(
    title="Network Monitor",
    version="0.0.1",
    description="""
    Web-сервис для анализа и мониторинга сетевых подключений на локальном компьютере
    """,
)

app.include_router(router_about_network)
app.include_router(router_eth_dump)


@app.post("/ping", )
async def ping(
    res: str = Query(
        description="IP-адрес сервера для проверки доступности (ping)",
        default="8.8.8.8",
    ),
    count_pkt: int = Query(
        description="Количество пакетов для проверки (ping)",
        default=1,
    )
) -> Dict[str, Any]:
    """
    Конечная точка для проверки состояния сервера путем пинга.

    :param res: IP-адрес сервера для пинга (по умолчанию: '8.8.8.8')
    :type res: str
    :param count_pkt: Количество пакетов для пинга (по умолчанию: 1)
    :type count_pkt: int

    :return: Словарь, содержащий количество загруженного и отправленного трафика на выбранном интерфейсе
    :rtype: dict
    """
    responce = await get_ping_status(res, count_pkt)
    return responce


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
