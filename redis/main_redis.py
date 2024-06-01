"""
# Entery point to 
"""

from initialize_redis import initialize_redis
from enginge_redis import create_redis_connect

if __name__ == "__main__":
    initialize_redis()
    client = create_redis_connect()
    client.hgetall("tg_id")
    client.hgetall("peer_nick")
