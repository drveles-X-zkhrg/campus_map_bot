"""
# Entery point to 
"""

import time
from backup_redis import redis_backup, redis_restore

# from initialize_redis import initialize_redis

if __name__ == "__main__":
    try:
        redis_restore()
        while True:
            redis_backup()
            time.sleep(3600)
    finally:
        pass
