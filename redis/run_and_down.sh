#!/bin/bash

# Function to handle termination signals
function handle_term {
  echo "Received termination signal. Creating backup..."
  /redis/backup.sh
  echo "Backup completed. Exiting..."
  exit 0
}


# Restore from the latest backup if available
/redis/restore.sh

# Trap termination signals
trap 'handle_term' SIGTERM SIGINT

# Start Redis server
redis-server --appendonly yes &

# Wait for Redis process to exit
wait $!
