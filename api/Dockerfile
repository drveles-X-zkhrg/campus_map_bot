FROM python:3.10.2

WORKDIR /api
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "app.main:app", "--host", "localhost", "--port", "8000"]