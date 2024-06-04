"""
## Initialize Redis DB if no backups
"""
import logging
from datetime import datetime
import redis

def initialize_redis():
    """
    ### Initialize Redis using default values
    """
    client = redis.Redis(host="localhost", port=6379, db=0)

    friends_data = {"tg_id": {"peer_nick1", "peer_nick2"}}
    for key, value in friends_data.items():
        client.hset(key, value)

    sessions_data = {
        "peer_nick": {
            "status": "1",
            "cluster": "init",
            "row": "a",
            "col": "1",
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
    }
    for key, value in sessions_data.items():
        client.hset(key, value)

    logging.warning("Start data has been initialized in Redis")
