# Friends Bot

## Parser ожидаемые проблемы.

1. Не хватило ресурсов и программа не выполнилась за минуту.
2. Не ответил сайт
3. Не удалось залогиниться
4. Не удалось загрузить карту кампуса
5. Не удалось развернуть этажи
6. Не удалось загрузить класстер 
7. Не удалось распрасить данные класстера.
8. Все класстеры пусты.

## TO DO

- Скрипт для установки окружения и зависимостей
    - установку питона,
    - установка окружения
    - переключение на окружение
    - стягивание рекваирментсов
    
<!-- - Крона или системцтл для автозапуска парсера. -->

- В код парсера неплохо бы встроить больше хендлеров ошибок, хотябы ручных. А лучше logging


## DOCs

вебдрайвер для линукс 
https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.60/linux64/chrome-linux64.zip

crontab 
*/1 * * * * cd /home/jenniffr/friends_bot/ && . /home/jenniffr/friends_bot/venv/bin/activate && /home/jenniffr/friends_bot/venv/bin/python3 /home/jenniffr/friends_bot/main.py >> /home/jenniffr/friends_bot/cron.log

### DB structure
s21 peer 
- id: int
- s21_nickname: char[128]

friend (many_to_many) 
- tg_id: int
- user: foreign_key(s21_peer)

cluster
- id: int
- name: char[128]

session
- id: int 
- user: foreign_key(s21_peer)
- online: bool
- cluster: foreign_key(cluster)
- row: char
- place: int
- timestamp: timestamp


## Idea

- Мне кажется проще всего в качестве доп функционала можно прикрутить уведомления - когда кто-то появился в кампусе, но это уже реально сталкеринг. Ну или платно.

