[![Deploy to Server](https://github.com/DrVeles/friends_bot/actions/workflows/deploy.yml/badge.svg?branch=develop)](https://github.com/DrVeles/friends_bot/actions/workflows/deploy.yml)
# Campus map bot

**Stack:** `Python`, `Redis`, `Docker`, `CI/CD`, `Linux` <br>
**Libraries:** `FastAPI`, `aiogram`, `asyncio`, `requests`, `logging`, `pydantic`, `re`

⚡ With this bot, you can find out if a student is on campus and what workplace he is at.

Описание на русском [здесь](./readme_rus.md).

## Features

✅ Create a list of friends to search for all at once. <br>
✅ Quick search by nickname.

## Project structure

The project consists of microservices. Each is located in its own *docker* container. All this is managed using *docker-compose*. <br>
<table>
  <tr>
    <td align="center">
      <img src="misc/containers_scheme.png" height="450" alt="Image 1">
    </td>
  </tr>
  <tr>
    <td>
      <p>diagram of how containers interact with each other within the network</p>
    </td>
  </tr>
</table>



### Frontend 
The service is responsible for the operation of the telegram-bot via REST API which is wrapped in a library for the python. Responsible for receiving data from the user, sending this data to the API, and sending responses. 

### Parser
The service parses data from the educational platform.
We log in to the platform and using the API of the School, we get the location data of the students and send it to our API in the form of *json*. 
  
### API
It serves as a link between all services:
- Accepts requests from frontend, accesses *Redis* and returns data about the requested students.
- Accepts new student data from the parser and updates records in *Redis*
  
### Redis
Stores data about students on campus and lists of friends in an impersonal form. It automatically makes a backup, and when the *docker* container is restarted, it starts from the previous backup.
  
## CI/CD
We use github actions to test the code, automatically deliver updates to the server.

## Usage example 
<table>
  <tr>
    <td align="center">
      <img src="misc/presentation.gif" height="600" alt="Image 1">
    </td>
  </tr>
  <tr>
    <td>
      <p>bot in usage</p>
    </td>
  </tr>
</table>

## Other | Links

[Try the bot](https://t.me/kzn_campus_map_bot ). Nickname example: `jenniffr` or `diamondp`.

Join the [discussion](https://github.com/DrVeles/campus_map_bot/discussions )

Report bugs in [issues](https://github.com/DrVeles/campus_map_bot/issues )
