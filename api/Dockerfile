FROM python:3.10.2-alpine3.15 AS builder

WORKDIR /api

ENV PYTHONDONTWRITEBYTECODE=1

COPY ./requirements.txt .

RUN apk add --update --virtual iputils-ping && \
    apk --no-cache add ca-certificates && \
    addgroup -S api && adduser --uid 19998 --shell /bin/false -S api -G api -h /home/api && \
    cat /etc/passwd | grep api > /etc/passwd_api && \
    pip install --upgrade cffi pip setuptools && \
    pip wheel --no-cache-dir --no-deps --wheel-dir /api/wheels -r requirements.txt && \
    find /usr/local \
    \( -type d -a -name test -o -name tests \) \
    -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
    -exec rm -rf '{}' +

FROM python:3.10.2-alpine3.15

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY --from=builder /etc/passwd_api /etc/passwd
COPY --from=builder /api/wheels /wheels
COPY --from=builder /api/requirements.txt .

RUN pip install --no-cache /wheels/* && mkdir -p /home/api && \
    chown -R api /home/api && \
    find /usr/local \
    \( -type d -a -name test -o -name tests \) \
    -o \( -type f -a -name '*.pyc' -o -name '*.pyo' -o -name '*.pyi' \) \
    -exec rm -rf '{}' +

COPY --chown=api . /home/api

USER api

WORKDIR /home/api

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "172.19.0.2", "--port", "8000"]
