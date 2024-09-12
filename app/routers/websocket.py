from fastapi import APIRouter, WebSocket
from typing import List

router = APIRouter()
connected_clients: List[WebSocket] = []


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            for client in connected_clients:
                await client.send_text(f"Message: {data}")
    except Exception as e:
        connected_clients.remove(websocket)
        await websocket.close()