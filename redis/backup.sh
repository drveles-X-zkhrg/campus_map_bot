#!/bin/bash
mkdir -p /backup

rm -rf /data/dump.rdb 

/usr/local/bin/redis-cli bgsave

rm -rf /backup/redis-backup.rdb

cp /data/dump.rdb /backup/redis-backup.rdb

while true; do
  sleep 1000
done 
