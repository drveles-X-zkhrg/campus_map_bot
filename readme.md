[![Deploy to Server](https://github.com/DrVeles/friends_bot/actions/workflows/deploy.yml/badge.svg?branch=develop)](https://github.com/DrVeles/friends_bot/actions/workflows/deploy.yml)
# Campus map bot

This bot allows you to find out if there is a person on campus and if so, where he/she is. 

## Features

- Create a list of friends to search all of them at once.
- Quick nickname search
  

## Project structure
The project consists of microservices. Each is in its own docker container.

### Frontend
This is where the bot logic is described

### Parser
Parses data from the education platform.
  

### API
Serves as a link between all services. 
  

### Redis
Stores necessary data. Automatically makes a backup.
  
### CI/CD
 We use github actions for testing code, automatic delivery of updates to the server.
## Other | Links

[Try bot](https://t.me/kzn_campus_map_bot). Example nickname: `jenniffr`.

Join the [discussion](https://github.com/DrVeles/campus_map_bot/discussions)

Report bugs in [issues](https://github.com/DrVeles/campus_map_bot/issues)
