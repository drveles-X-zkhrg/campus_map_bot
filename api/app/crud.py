"""CRUD operations backed by Redis."""

import json

from app import database, schemas, transactions
import redis

redis_client = database.get_redis_client()


def create_friend_pair(friend_pair: schemas.FriendsByTelegramID) -> str:
    """Add a peer nickname to a Telegram user's friends set."""
    redis_client.sadd(friend_pair.tg_id, friend_pair.peer_name)
    return "ok"


def delete_friend_pair(friend_pair: schemas.FriendsByTelegramID) -> str:
    """Remove a peer nickname from a Telegram user's friends set."""
    redis_client.srem(friend_pair.tg_id, friend_pair.peer_name)
    return "ok"


def update_peers(peers_dict: schemas.PeersDict) -> str:
    """Replace the current peer snapshot in Redis."""
    try:
        redis_client.watch(database.PEERS_KEY)
        peers_json = peers_dict.json()
        peers_data = json.loads(peers_json)
        transactions.update_peers(
            redis_client, database.PEERS_KEY, peers_data[database.PEERS_KEY]
        )
        return "ok"
    except redis.WatchError:
        redis_client.unwatch()
        return "not ok"
    except (redis.RedisError, json.JSONDecodeError, KeyError, TypeError, ValueError) as err:
        print(f"An error occurred: {err}")
        return "not ok"


def get_friends_status(tg_id: schemas.TelegramID) -> schemas.PeersDict:
    """Return status data for all peers in a Telegram user's friends list."""
    friend_names = redis_client.smembers(tg_id.tg_id)
    answer: schemas.PeersDict = schemas.PeersDict()
    for name in friend_names:
        peer: schemas.Peer = schemas.Peer.parse_obj(redis_client.hgetall(name))
        print(peer)
        answer.peers[name] = peer

    del answer.peers[""]

    return answer


def get_peer_status(peer_name: schemas.PeerName) -> schemas.PeersDict:
    """Return status data for a single peer nickname."""
    answer: schemas.PeersDict = schemas.PeersDict()
    peer: schemas.Peer = schemas.Peer.parse_obj(
        redis_client.hgetall(peer_name.peer_name)
    )
    answer.peers[peer_name.peer_name] = peer

    del answer.peers[""]

    return answer
