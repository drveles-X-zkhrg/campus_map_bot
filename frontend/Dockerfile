FROM python:3.10.2
RUN apt update && apt install iputils-ping -y

WORKDIR /frontend
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1

CMD ["python3", "main.py"]
