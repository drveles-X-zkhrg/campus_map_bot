FROM dockerhub.timeweb.cloud/library/python:3.10.2

WORKDIR /frontend
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80 443

# ENV NAME World

ENV PYTHONUNBUFFERED=1

RUN echo "BUILD SUCCESS"
CMD ["python3", "main.py"]
