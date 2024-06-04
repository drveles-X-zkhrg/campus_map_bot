"""
## Backuping Redis 
"""

import os
import shutil
import time
import logging
from enginge_redis import create_redis_connect
import redis

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()


def redis_backup():
    """
    ### Backup Redis DB
    """
    r = create_redis_connect()

    backup_dir = "/backups"
    os.makedirs(backup_dir, exist_ok=True)
    try:
        r.save()
        time.sleep(5)
        redis_dump_file = "/data/dump.rdb"
        if not os.path.exists(redis_dump_file):
            raise FileNotFoundError(f"Redis dump file not found at {redis_dump_file}")
        backup_file = os.path.join(backup_dir, "redis_backup.rdb")
        shutil.copy2(redis_dump_file, backup_file)
        logger.info("Backup created at %s", backup_file)

    except (redis.RedisError, IOError, FileNotFoundError) as ex:
        logger.error("An error occurred: %s", ex)


def redis_restore(backup_file="/backups/redis_backup.rdb"):
    """
    ### Restore Redis DB from Backup
    """
    r = create_redis_connect()
    if not os.path.exists(backup_file):
        logger.error("Backup file not found: %s", backup_file)
        return False

    try:
        r.shutdown(save=False)
        time.sleep(5)
        redis_dump_file = "/data/dump.rdb"
        shutil.copy2(backup_file, redis_dump_file)
        r = create_redis_connect()
        logger.info("Restored Redis from backup: %s", backup_file)
        return True
    except (redis.RedisError, IOError, FileNotFoundError) as ex:
        logger.error("An error occurred while restoring: %s", ex)


if __name__ == "__main__":
    redis_backup()
