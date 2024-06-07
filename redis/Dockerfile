FROM redis:latest

RUN apt-get update && apt-get install -y cron

WORKDIR /redis
COPY . .
RUN chmod +x backup.sh restore.sh run_and_down.sh

# Add cron job for periodic backups (every 10 minute)
RUN (crontab -l ; echo "*/10 * * * * /redis/backup.sh") | crontab
