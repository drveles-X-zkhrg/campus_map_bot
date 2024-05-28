import os
from dotenv import load_dotenv

"""
Getting data to BD engine from .env

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

load_dotenv()

DB_URL_SQLITE = os.getenv("DB_URL_SQLITE")

engine_lite = sqlalchemy.create_engine(
    url=DB_URL_SQLITE,
    echo=False,
)

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT", 5432)  # Устанавливаем порт по умолчанию 5432
DB_URL_PG = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine_pg = sqlalchemy.create_engine(
    url=DB_URL_PG,
    echo=False,
)

engine = engine_lite
# engine = engine_pg
# switch to needed engine

Session = sessionmaker(bind=engine)
