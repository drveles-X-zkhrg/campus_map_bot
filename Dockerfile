# Используйте официальный базовый образ Python 3.10.2
FROM python:3.10.2

# Установите рабочую директорию в контейнере
WORKDIR /app

# Установите ChromeDriver
RUN CHROME_DRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    rm /tmp/chromedriver.zip

# Скопируйте файл requirements.txt в рабочую директорию
COPY requirements.txt .

# Установите зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте остальной исходный код в рабочую директорию
COPY . .

# Определите команду, которая будет выполняться при запуске контейнера
CMD ["python", "main.py"]

