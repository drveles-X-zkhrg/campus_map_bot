import redis
from typing import Dict


def update_peers(r: redis.StrictRedis, set_name: str, h: Dict):
    old_peers = r.smembers(set_name)
    pipe = r.pipeline()
    for old_peer in old_peers:
        pipe.hset(old_peer, "status", "0")

    for el in h:
        pipe.sadd(set_name, el)
        pipe.hset(el, mapping=h[el])

    pipe.execute()
