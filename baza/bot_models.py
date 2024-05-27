"""
Here only a description of the database and its tables
"""

from sqlalchemy import (
    Table,
    Column,
    Boolean,
    Integer,
    CHAR,
    String,
    TIMESTAMP,
    ForeignKey,
    MetaData,
)
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

DB_URL = dotenv_values(".env").get("DB_URL")

metadata_objs = MetaData()

s21_peer_table = Table(
    "s21_peers",
    metadata_objs,
    Column("id", Integer, primary_key=True),
    Column("s21_nickname", String),
)

friends_table = Table(
    "friends",
    metadata_objs,
    Column("tg_id", Integer),
    Column("friend", Integer, ForeignKey("s21_peers.id")),
)

cluster_table = Table(
    "clusters",
    metadata_objs,
    Column("id", Integer, primary_key=True),
    Column("name", String),
)

session_table = Table(
    "sessions",
    metadata_objs,
    Column("id", Integer, primary_key=True),
    Column("peer_id", Integer, ForeignKey("s21_peers.id")),
    Column("online", Boolean),
    Column("cluster_id", Integer, ForeignKey("clusters.id")),
    Column("row", CHAR),
    Column("place", Integer),
    Column("timestamp", TIMESTAMP),
)
