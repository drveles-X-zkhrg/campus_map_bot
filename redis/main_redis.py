from initialize_redis import *

if __name__ == "__main__":
    initialize_redis()
    client = redis.Redis(host="localhost", port=6379, db=0)
    client.hgetall("tg_id")
    client.hgetall("peer_nick")
   