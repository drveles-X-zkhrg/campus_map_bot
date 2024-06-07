#!/bin/bash

BACKUP_DIR=/backup
LATEST_BACKUP=$(ls -t $BACKUP_DIR/*.rdb | head -n 1)

if [ -f "$LATEST_BACKUP" ]; then
  cp $LATEST_BACKUP /data/dump.rdb
fi

echo "restore "$LATEST_BACKUP" complete"
exec redis-server --appendonly yes