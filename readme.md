[![Deploy to Server](https://github.com/DrVeles/friends_bot/actions/workflows/deploy.yml/badge.svg?branch=develop)](https://github.com/DrVeles/friends_bot/actions/workflows/deploy.yml)
# Campus map bot

**Stack:** `Python`, `Redis`, `Docker`, `CI/CD`, `Linux` <br>
**Libraries:** `FastAPI`, `aiogram`, `asyncio`, `requests`, `selenium`, `logging`, `pydantic`, `re`

⚡ With this bot, you can find out if a student is on campus and what workplace he is at.

Описание на русском [здесь](./readme_rus.md).

## Features

✅ Create a list of friends to search for all at once. <br>
✅ Quick search by nickname.

## Project structure

The project consists of microservices. Each is located in its own *docker* container. All this is managed using *docker-compose*. 

### Frontend 
The service is responsible for the operation of the bot. Responsible for receiving data from the user, sending this data to the API, and sending responses. 

### Parser
The service parses data from the educational platform.
Automatic authorization is configured, bypassing the campus map and saving data as html pages. Using regular expressions, we get the students' location data and send it to the API in the form of *json*. 
  
### API
It serves as a link between all services:
- Accepts requests from frontend, accesses *Redis* and returns data about the requested students.
- Accepts new student data from the parser and updates records in *Redis*
  
### Redis
Stores data about students on campus and lists of friends in an impersonal form. It automatically makes a backup, and when the *docker* container is restarted, it starts from the previous backup.
  
## CI/CD
We use github actions to test the code, automatically deliver updates to the server.
 
## Other | Links

[Try the bot](https://t.me/kzn_campus_map_bot ). Nickname example: `jenniffr` or `diamondp`.

Join the [discussion](https://github.com/DrVeles/campus_map_bot/discussions )

Report bugs in [issues](https://github.com/DrVeles/campus_map_bot/issues )
