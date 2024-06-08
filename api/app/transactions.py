import redis
from typing import Dict


def update_peers(r: redis.StrictRedis, set_name: str, h: Dict):
    pipe = r.pipeline()
    old_peers = pipe.smembers(set_name)
    for old_peer in old_peers:
        pipe.hset(old_peer, "status", "0")

    for el in h:
        pipe.sadd(set_name, el)
        pipe.hmset(el, h[el])

    pipe.execute()
