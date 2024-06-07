FROM redis:latest

RUN apt-get update && apt-get install -y cron

# ADD crontab /etc/cron.d/autobackup

# RUN chmod 0644 /etc/cron.d/autobackup
# RUN crontab /etc/cron.d/autobackup
# RUN touch /var/log/cron.log


RUN echo "*/1 * * * * /bin/sh /redis/backup.sh >> /var/log/cron.log 2>&1 && echo 'auto backuped'" >> /etc/crontab

RUN touch /var/log/cron.log

WORKDIR /redis
COPY . .
RUN chmod +x *.sh

# Run the command on container startup
# RUN cron && tail -f /var/log/cron.log 
CMD ["bash", "-c", "/redis/restore.sh && cron && tail -f /var/log/cron.log"]