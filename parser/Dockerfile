FROM python:3.10.2

WORKDIR /parser
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1
ENV DISPLAY=:99

CMD ["python3", "main.py"]
