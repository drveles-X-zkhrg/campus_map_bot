import redis
from datetime import datetime

def initialize_redis():

    client = redis.Redis(host="localhost", port=6379, db=0)

    friends_data = {"tg_id": {"peer_nick", "peer_nick"}}
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

    print("Data has been initialized in Redis")
