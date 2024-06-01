import uuid
from typing import List, Optional
from pydantic import BaseModel
from app.database import get_redis_client

redis_client = get_redis_client()


class FriendPairModel(BaseModel):
    id: str
    tg_id: int
    peer_name: str

    @classmethod
    def create(cls, tg_id: int, peer_name: str) -> 'FriendPairModel':
        pair_id = str(uuid.uuid4())
        pair_data = {"id": pair_id, "tg_id": tg_id, "peer_name": peer_name}
        redis_client.hset(pair_id, mapping=pair_data)
        return cls(**pair_data)

    @classmethod
    def get(cls, pair_id: str) -> Optional['FriendPairModel']:
        pair_data = redis_client.hgetall(
            "9c8265b3-6db1-489b-9b1f-207840eb2560")
        print(redis_client.keys(pattern='*'))
        print(pair_data)
        if not pair_data:
            return None
        return cls(id=pair_id, **pair_data)

    @classmethod
    def get_all(cls) -> List['FriendPairModel']:
        keys = redis_client.keys()
        pairs = []
        for key in keys:
            pair_data = redis_client.hgetall(key)
            pair = cls(id=key, **pair_data)
            pairs.append(pair)
        return pairs
