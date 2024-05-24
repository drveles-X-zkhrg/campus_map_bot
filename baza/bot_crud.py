from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from bot_models import *
from bot_creating_db import *

def create_all_kzn_clusters(): 
    engine = create_engine(url=DB_URL, echo=True)
    Session = sessionmaker(bind=engine)

    # хочу все это запихать в блок try

    with Session() as session:
        cluster_names = ["et", "ev", "si", "ge", "pr", "un", "va"]
        for cluster_name in cluster_names:
            cluster = cluster_table.insert().values(name=cluster_name)
            session.execute(cluster)
        
        session.commit()


def update_peers_sessions(peers_sessions): 
    engine = create_engine(url=DB_URL, echo=True)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        # Вставка нового s21_peer
        peer = s21_peer_table.insert().values(s21_nickname="jenniffr")
        result = session.execute(peer)
        session.commit()
        peer_id = result.inserted_primary_key[0]

        # Получение id кластера 'va'
        cluster_id = session.execute(select(cluster_table.c.id).where(cluster_table.c.name == "va")).scalar()

        # Вставка данных в таблицу session
        session_data = {
            "peer": peer_id,
            "online": False,
            "cluster": cluster_id,
            "row": "g",
            "place": 1,
            "timestamp": "2023-10-01 00:00:00"  # Замените на актуальную временную метку
        }
        session.execute(session_table.insert().values(**session_data))

        session.commit()


if __name__ == "__main__":
    create_all_tables()
    # create_all_kzn_clusters()