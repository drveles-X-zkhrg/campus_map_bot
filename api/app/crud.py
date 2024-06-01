import redis
import json
import uuid
from datetime import datetime
from app import schemas
from app import database
from app import transactions

redis_client = database.get_redis_client()


def create_friend_pair(friend_pair: schemas.FriendsByTelegramID) -> str:
    # если редиска отвалилась нужно хендлить
    redis_client.sadd(friend_pair.tg_id, friend_pair.peer_name)
    return 'ok'


def delete_friend_pair(friend_pair: schemas.FriendsByTelegramID) -> str:
    # если редиска отвалилась нужно хендлить
    redis_client.srem(friend_pair.tg_id, friend_pair.peer_name)
    return 'ok'


def update_peers(peers_dict: schemas.PeersDict) -> str:
    try:
        # Отметка ключа для наблюдения
        redis_client.watch(database.PEERS_KEY)
        pdj = peers_dict.json()
        pdd = json.loads(pdj)
        transactions.transa(redis_client, database.PEERS_KEY,
                            pdd[database.PEERS_KEY])

        # Применение транзакции
        return "ok"
    except redis.WatchError:
        redis_client.unwatch()  # Сбрасываем наблюдение перед следующей попыткой
    except Exception as e:
        print(f"An error occurred: {e}")
        return "not ok"
    # print(peers_dict.json())
    pdj = peers_dict.json()
    pdd = json.loads(pdj)
    # pdj = json.dumps(pdd)
    # redis_client.hmset(database.PEERS_KEY, {database.PEERS_KEY: pdj})
    # return 'ok'
