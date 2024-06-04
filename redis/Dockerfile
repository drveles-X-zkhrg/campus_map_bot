FROM dockerhub.timeweb.cloud/library/redis:latest

FROM dockerhub.timeweb.cloud/library/python:3.10.2

WORKDIR /redis
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1

CMD ["python3", "main.py"]
