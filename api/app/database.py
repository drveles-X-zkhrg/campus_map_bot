"""Redis connection settings and client factory."""

import os

import redis

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = 6379
REDIS_DB = 0
PEERS_KEY = "peers"


def get_redis_client() -> redis.StrictRedis:
    """Create and return a Redis client with decoded string responses."""
    return redis.StrictRedis(
        host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True
    )
