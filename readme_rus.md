[![Deploy to Server](https://github.com/DrVeles/friends_bot/actions/workflows/deploy.yml/badge.svg?branch=develop)](https://github.com/DrVeles/friends_bot/actions/workflows/deploy.yml)
# Campus map bot

**Стек:** `Python`, `Redis`, `Docker`, `CI/CD`, `Linux` <br>
**Библиотеки:** `FastAPI`, `aiogram`, `asyncio`, `requests`, `logging`, `pydantic`, `re`<br>

⚡ С помощью этого бота можно узнать в кампусе ли студент и за каким рабочим местом находится.

English readme [here](./readme.md).

## Features

✅ Создание списка друзей, для поиска по всем сразу. <br>
✅ Быстрый поиск по нику.

## Project structure

Проект состоит из микросервисов. Каждый находится в собственном *docker* контейнере. Все это управляется с помощью *docker-compose*. 

### Frontend 
Сервис отвечает за работу бота. Отвечает за прием данных от пользователя, отправку этих данных в API, рассылку ответов. 

### Parser
Сервис парсит данные с образовательной платформы.
Авторизуемся на платформе и используя API Школы 21 достаем данные о местоположении студентов и отправляем их в наш API в виде *json*. 
  
### API
Служит связующим звеном между всеми сервисами:
- Принимает запросы с frontend'a, обращается к *Redis* и возвращает данные о запрашиваемых студентах.
- Принимает новые данные о студентах с parser'a и обновляет записи в *Redis*
  
### Redis
Хранит данные о студентах в кампусе и списки друзей в обезличенном виде. Автоматически делает бекап, а при рестарте *docker* контейнера запускается с предыдущего бекапа.
  
## CI/CD
 Мы используем github actions для тестирования кода, автоматической доставки обновлений на сервер.
 
## Other | Links

[Попробовать бота](https://t.me/kzn_campus_map_bot). Пример ника: `jenniffr`

Присоединяйтесь к [обсуждению](https://github.com/DrVeles/campus_map_bot/discussions).

Сообщайте об ошибках в [issues](https://github.com/DrVeles/campus_map_bot/issues).
