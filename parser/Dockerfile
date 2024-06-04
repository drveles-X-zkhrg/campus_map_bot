FROM python:3.10.2

RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver 

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /parser
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN cp /usr/bin/chromedriver /parser/

ENV PYTHONUNBUFFERED=1
ENV DISPLAY=:99

CMD ["python3", "main.py"]
