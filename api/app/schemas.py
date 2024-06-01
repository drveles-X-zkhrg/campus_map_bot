from pydantic import BaseModel
from typing import Dict
from datetime import datetime


class FriendsByTelegramID(BaseModel):
    tg_id: int
    peer_name: str


class Peer(BaseModel):
    row: str = ""
    col: str = ""
    cluster: str = ""
    time: datetime = datetime.now()
    status: int = 0


class TelegramID(BaseModel):
    tg_id: int


class PeersDict(BaseModel):
    peers: Dict[str, Peer] = {"": Peer()}
