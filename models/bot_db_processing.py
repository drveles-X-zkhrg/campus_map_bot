import sqlalchemy
from bot_models import *


def testing():
    engine = sqlalchemy.create_engine(
        # here need switch to other cool BD
        url="sqlite:///venv/db/example.db",
        echo=True
    )
    metadata_objs.create_all(engine)
    

if __name__ == "__main__":
    testing()
