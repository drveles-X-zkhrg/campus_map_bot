FROM redis:latest

WORKDIR /redis
COPY . .

CMD [ "sh", "-c", "redis-server /redis/redis.conf" ]