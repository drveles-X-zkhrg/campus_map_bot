#!/bin/bash

cp -rf /backup/redis-backup.rdb /data/dump.rdb

echo "restore backup complete"

echo | crontab -l ;

exec redis-server