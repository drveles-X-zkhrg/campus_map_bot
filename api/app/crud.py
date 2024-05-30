import redis
import uuid
from app import schemas
from app import database
from app.models import FriendPairModel

redis_client = database.get_redis_client()


def create_friend_pair(friend_pair: schemas.FriendPairSchema) -> FriendPairModel:
    return FriendPairModel.create(tg_id=friend_pair.tg_id, peer_name=friend_pair.peer_name)


def get_friend_pair(pair_id: str) -> FriendPairModel:
    return FriendPairModel.get(pair_id=pair_id)
