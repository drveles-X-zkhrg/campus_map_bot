FROM python:3.10.2

RUN apt update && apt install iputils-ping -y

WORKDIR /api
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "app.main:app", "--host", "172.19.0.2", "--port", "8000"]