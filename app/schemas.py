from pydantic import BaseModel


class FriendId(BaseModel):
    tg_id: int
    peer_id: str


class ItemCreate(ItemBase):
    pass

#


class Item(ItemBase):
    id: str

    class Config:
        orm_mode = True
