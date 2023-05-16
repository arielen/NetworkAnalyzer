from typing import Annotated
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
    Web service for analyzing and monitoring network connections on a local computer.
    """,
)

app.include_router(router_about_network)
app.include_router(router_eth_dump)



@app.post("/ping")
async def ping(res: str = "8.8.8.8", count_pkt: int = 1) -> dict:
    """
    Endpoint to check the status of the server by pinging it.
    """
    responce = await get_ping_status(res, count_pkt)
    return responce


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
