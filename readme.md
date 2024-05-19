# Friends Bot

## TO DO

- Скрипт для установки окружения и зависимостей
    - установку питона,
    - установка окружения
    - переключение на окружение
    - стягивание рекваирментсов
    
- Крона или системцтл для автозапуска парсера.

- В код парсера неплохо бы встроить больше хендлеров ошибок, хотябы ручных. 

## DOCs

вебдрайвер для линукс 
https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.60/linux64/chrome-linux64.zip

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