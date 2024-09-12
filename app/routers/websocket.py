from fastapi import APIRouter, WebSocket
from typing import List

router = APIRouter()
connected_clients: List[WebSocket] = []