import sqlalchemy
from bot_models import *

engine_lite = sqlalchemy.create_engine(
        url=DB_URL,
        echo=True,
    )

engine_pg = None
# here we can switch to other cool BD

def create_all_tables():
    metadata_objs.create_all(engine_lite)

def drop_all_tables():
    metadata_objs.drop_all(engine_lite)

if __name__ == "__main__":
    create_all_tables()
