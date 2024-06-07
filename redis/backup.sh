#!/bin/bash

BACKUP_DIR=/backup
BACKUP_NAME=redis-backup.rdb
REDIS_CLI=/usr/local/bin/redis-cli

# Create backup directory if not exists
mkdir -p $BACKUP_DIR

# Save the current DB
$REDIS_CLI SAVE

# Copy the dump.rdb to backup directory with a timestamp
cp /data/dump.rdb $BACKUP_DIR/$BACKUP_NAME
