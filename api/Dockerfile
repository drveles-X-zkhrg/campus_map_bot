FROM dockerhub.timeweb.cloud/library/python:3.10.2

WORKDIR /api
COPY . .

RUN python3 -m venv venv
RUN /bin/bash -c "source venv/bin/activate"
RUN ls
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]