"""Pydantic models for API request and response payloads."""

# pylint: disable=too-few-public-methods

from datetime import datetime, timedelta, timezone
from typing import Dict

from pydantic import BaseModel, Field

MOSCOW_TIMEZONE = timezone(timedelta(hours=3))


class FriendsByTelegramID(BaseModel):
    """Link between a Telegram user and a peer nickname."""

    tg_id: int
    peer_name: str


class Peer(BaseModel):
    """Campus map location and online status for a peer."""

    row: str = ""
    col: str = ""
    cluster: str = ""
    time: datetime = Field(
        default_factory=lambda: datetime.now(tz=MOSCOW_TIMEZONE).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    )
    status: str = "0"


class TelegramID(BaseModel):
    """Telegram user identifier."""

    tg_id: int


class PeerName(BaseModel):
    """Peer nickname lookup key."""

    peer_name: str


class PeersDict(BaseModel):
    """Dictionary of peers keyed by nickname."""

    peers: Dict[str, Peer] = {"": Peer()}
