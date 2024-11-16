FROM python:3.10.2-alpine3.15 AS builder

WORKDIR /frontend

ENV PYTHONDONTWRITEBYTECODE=1

COPY ./requirements.txt .

RUN apk add --update --virtual iputils-ping && \
    apk --no-cache add ca-certificates && \
    addgroup -S frontend && adduser --uid 19998 --shell /bin/false -S frontend -G frontend -h /home/frontend && \
    cat /etc/passwd | grep frontend > /etc/passwd_frontend && \
    pip install --upgrade cffi pip setuptools && \
    pip wheel --no-cache-dir --no-deps --wheel-dir /frontend/wheels -r requirements.txt && \
    find /usr/local \
    \( -type d -a -name test -o -name tests \) \
    -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
    -exec rm -rf '{}' +

FROM python:3.10.2-alpine3.15

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY --from=builder /etc/passwd_frontend /etc/passwd
COPY --from=builder /frontend/wheels /wheels
COPY --from=builder /frontend/requirements.txt .

RUN pip install --no-cache /wheels/* && mkdir -p /home/frontend && \
    chown -R frontend /home/frontend && \
    find /usr/local \
    \( -type d -a -name test -o -name tests \) \
    -o \( -type f -a -name '*.pyc' -o -name '*.pyo' -o -name '*.pyi' \) \
    -exec rm -rf '{}' +

COPY --chown=frontend . /home/frontend

USER frontend

WORKDIR /home/frontend

CMD ["python3", "main.py"]
