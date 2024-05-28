# Friends Bot

## TO DO

- Скрипт для установки окружения и зависимостей
    - установку питона,
    - установка окружения
    - переключение на окружение
    - стягивание рекваирментсов
    
- В код парсера неплохо бы встроить больше хендлеров ошибок, хотябы ручных. А лучше logging


## DOCs

Вебдрайвер должен лежать в `.venv/`

вебдрайвер для линукс 
https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.60/linux64/chrome-linux64.zip

<!-- - Крона или системцтл для автозапуска парсера. -->
crontab 
*/1 * * * * cd /home/jenniffr/friends_bot/ && . /home/jenniffr/friends_bot/venv/bin/activate && /home/jenniffr/friends_bot/venv/bin/python3 /home/jenniffr/friends_bot/main.py >> /home/jenniffr/friends_bot/cron.log

scp jenniffr@87.242.85.185:/home/jenniffr/friends_bot/cron.log ./
