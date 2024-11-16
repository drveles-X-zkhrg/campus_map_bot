FROM python:3.10.2-alpine3.15 AS builder

WORKDIR /parser

ENV PYTHONDONTWRITEBYTECODE=1

COPY ./requirements.txt .

RUN addgroup -S parser && adduser --uid 19998 --shell /bin/false -S parser -G parser -h /home/parser && \
    cat /etc/passwd | grep parser > /etc/passwd_parser && \
    pip install --upgrade cffi pip setuptools && \
    pip wheel --no-cache-dir --no-deps --wheel-dir /parser/wheels -r requirements.txt && \
    find /usr/local \
    \( -type d -a -name test -o -name tests \) \
    -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
    -exec rm -rf '{}' +


FROM python:3.10.2-alpine3.15

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DISPLAY=:99

COPY --from=builder /etc/passwd_parser /etc/passwd
COPY --from=builder /parser/wheels /wheels
COPY --from=builder /parser/requirements.txt .

RUN pip install --no-cache /wheels/* && mkdir -p /home/parser && \
    chown -R parser /home/parser && \
    find /usr/local \
    \( -type d -a -name test -o -name tests \) \
    -o \( -type f -a -name '*.pyc' -o -name '*.pyo' -o -name '*.pyi' \) \
    -exec rm -rf '{}' +

COPY --chown=parser . /home/parser

USER parser

WORKDIR /home/parser

CMD ["python3", "main.py"]
