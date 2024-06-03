FROM dockerhub.timeweb.cloud/library/python:3.10.2

RUN apt-get update && apt-get install -y \
    chromium-driver \
    wget \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /parser

RUN python3 -m venv venv
RUN cp /usr/bin/chromedriver /parser/venv/bin/
COPY requirements.txt /parser/requirements.txt
RUN . /parser/venv/bin/activate && pip install --no-cache-dir -r /parser/requirements.txt
COPY . .

ENV PYTHONUNBUFFERED=1
ENV DISPLAY=:99

CMD ["python","parser_main.py"]