import redis
from typing import Dict


def transa(r: redis.StrictRedis, set_name: str, h: Dict):
    pipe = r.pipeline()
    for el in h:
        pipe.sadd(set_name, el)
        pipe.hmset(el, h[el])

    pipe.execute()
