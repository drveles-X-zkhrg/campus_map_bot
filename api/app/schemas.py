from pydantic import BaseModel, Field
from typing import Dict
from datetime import datetime, timezone, timedelta

moscow_timezone = timezone(timedelta(hours=3))

class FriendsByTelegramID(BaseModel):
    tg_id: int
    peer_name: str


class Peer(BaseModel):
    row: str = ""
    col: str = ""
    cluster: str = ""
    time: datetime = Field(default_factory=lambda: datetime.now(tz=moscow_timezone).strftime("%Y-%m-%d %H:%M:%S"))
    status: str = "0"

class TelegramID(BaseModel):
    tg_id: int


class PeerName(BaseModel):
    peer_name: str


class PeersDict(BaseModel):
    peers: Dict[str, Peer] = {"": Peer()}
