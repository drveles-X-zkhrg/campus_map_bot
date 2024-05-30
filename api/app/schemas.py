from pydantic import BaseModel


class FriendPairSchema(BaseModel):
    tg_id: int
    peer_name: str


class F(BaseModel):
    peer_id: str


# class Peer(BaseModel):
#     peer_name: str
#     status: bool
#     time: datetime
#     row: str
#     col: str
