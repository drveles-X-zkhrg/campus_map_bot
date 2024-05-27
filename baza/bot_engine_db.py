from dotenv import dotenv_values

"""
Gettin login and pass from .env file to edu.21-school.ru

File format for postgreSQL:
    DB_NAME=your_database_name
    DB_USER=your_username
    DB_PASSWORD=your_password
    DB_HOST=your_host
    DB_PORT=5432

File format for SQLite:
    DB_URL=you_path_to_DB
"""
import sqlalchemy
from sqlalchemy.orm import sessionmaker

DB_URL = dotenv_values(".env").get("DB_URL")

engine_lite = sqlalchemy.create_engine(
    url=DB_URL,
    echo=True,  # off it before release
)

# engine_pg = None
# here we can switch to other cool BD


engine = engine_lite  # switch to needed engine

Session = sessionmaker(bind=engine)
