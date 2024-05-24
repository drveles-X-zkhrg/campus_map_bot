import sqlalchemy
from bot_models import *


def create_all_tables():
    engine = sqlalchemy.create_engine(
        # here we can switch to other cool BD
        url=DB_URL,
        echo=True,
    )
    metadata_objs.create_all(engine)


if __name__ == "__main__":
    create_all_tables()
