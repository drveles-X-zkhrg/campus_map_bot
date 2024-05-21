from sqlalchemy import Table, Column, Boolean, Integer, CHAR, String, TIMESTAMP, ForeignKey, MetaData

metadata_objs = MetaData()

s21_peer_table = Table (
    "s21_peer", 
    metadata_objs,
    Column("id", Integer, primary_key=True),
    Column("s21_nickname", String),
)

friends_table = Table(
    "friends",
    metadata_objs,
    Column("tg_id", Integer),
    Column("friend", Integer, ForeignKey("s21_peer.id")), 
)


cluster_table = Table(
    "cluster",
    metadata_objs,
    Column("id", Integer, primary_key=True),
    Column("name", String),
)

session_table = Table(
    "session",
    metadata_objs,
    Column("id", Integer, primary_key=True),
    Column("peer", Integer, ForeignKey("s21_peer.id")), 
    Column("online", Boolean),
    Column("cluster", Integer, ForeignKey("cluster.id")), 
    Column("row", CHAR),
    Column("place", Integer),
    Column("timestamp", TIMESTAMP),
)