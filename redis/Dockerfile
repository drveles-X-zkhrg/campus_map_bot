FROM dockerhub.timeweb.cloud/library/redis:latest
FROM dockerhub.timeweb.cloud/library/python:3.10.2

WORKDIR /redis
COPY . .

RUN python3 -m venv venv
RUN /bin/bash -c "source venv/bin/activate"
RUN pip install --no-cache-dir -r requirements.txt


CMD ["python3", "main_redis.py"]
