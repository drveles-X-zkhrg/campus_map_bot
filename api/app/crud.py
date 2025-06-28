import redis
import json
from app import schemas
from app import database
from app import transactions

redis_client = database.get_redis_client()


def create_friend_pair(friend_pair: schemas.FriendsByTelegramID) -> str:
    redis_client.sadd(friend_pair.tg_id, friend_pair.peer_name)
    return "ok"


def delete_friend_pair(friend_pair: schemas.FriendsByTelegramID) -> str:
    redis_client.srem(friend_pair.tg_id, friend_pair.peer_name)
    return "ok"


def update_peers(peers_dict) -> str:
    try:
        redis_client.watch(database.PEERS_KEY)
        pdj = peers_dict.json()
        pdd = json.loads(pdj)
        transactions.update_peers(
            redis_client, database.PEERS_KEY, pdd[database.PEERS_KEY]
        )
        return "ok"
    except redis.WatchError:
        redis_client.unwatch()
    except Exception as e:
        print(f"An error occurred: {e}")
        return "not ok"


def get_friends_status(tg_id: schemas.TelegramID) -> schemas.PeersDict:
    friend_names = redis_client.smembers(tg_id.tg_id)
    answer: schemas.PeersDict = schemas.PeersDict()
    for name in friend_names:
        peer: schemas.Peer = schemas.Peer.parse_obj(redis_client.hgetall(name))
        print(peer)
        answer.peers[name] = peer

    del answer.peers[""]

    return answer


def get_peer_status(peer_name: schemas.PeerName) -> schemas.PeersDict:
    answer: schemas.PeersDict = schemas.PeersDict()
    peer: schemas.Peer = schemas.Peer.parse_obj(
        redis_client.hgetall(peer_name.peer_name)
    )
    answer.peers[peer_name.peer_name] = peer

    del answer.peers[""]

    return answer
