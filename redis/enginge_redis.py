"""
## Initialize connetion to Redis DB
"""
import os
from dotenv import load_dotenv
import redis

def create_redis_connect() -> redis.StrictRedis:
    """
    ### Initialize and return connection

    Getting data to BD connetion from .env
    File format for Redis:
        DB_HOST=your_host
        DB_PORT=5432
        REDIS_DB=num_of_database_in_redis
    """
    load_dotenv()
    redis_host = os.getenv("REDIS_HOST") or 'localhost'
    redis_port = int(os.getenv("REDIS_PORT")) or 6379
    redis_db = int(os.getenv("REDIS_DB")) or 0

    return redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)
