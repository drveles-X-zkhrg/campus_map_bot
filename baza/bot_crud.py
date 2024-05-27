from sqlalchemy import select, update, func
from sqlalchemy.orm import sessionmaker
from bot_models import *
from bot_creating_db import *
import time

def create_all_kzn_clusters():
    """
    ## Initializating clusters for KZN campus. 
    It is executed once, immediately after creating the tables.
    """
    try:
        Session = sessionmaker(bind=engine_lite)
        with Session() as session:
            cluster_names = ["et", "ev", "si", "ge", "pr", "un", "va"]
            for cluster_name in cluster_names:
                existing_cluster = session.execute(
                    select(cluster_table.c.id).where(cluster_table.c.name == cluster_name)
                ).fetchone()

                if not existing_cluster:
                    cluster = cluster_table.insert().values(name=cluster_name)
                    session.execute(cluster)
            
            session.commit()

        print("All clusters for KZN campus created")
    except Exception as ex:
        print(ex)

def update_peers_sessions(peers_sessions):
    """
    ## This func update sessions info in DB 

    Inputed:
    `peers in cluster:` {(nick, cluster_name, row_char, row_int), ...}
    """
 
    try:
        # произошла атомарность 
        Session = sessionmaker(bind=engine_lite)

        with Session() as session:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                         
            for peer_nick, peer_cluster, peer_row, peer_place in peers_sessions:
                print(peer_nick, peer_cluster, peer_row, peer_place )
                print(peer_nick, peer_cluster, peer_row, peer_place )
                print(peer_nick, peer_cluster, peer_row, peer_place )
                s21_peer = session.execute(select(s21_peer_table.c.id).where(s21_peer_table.c.s21_nickname == peer_nick)).fetchone()
                if s21_peer:
                    peer_id_temp = s21_peer[0]
                else:
                    new_peer = s21_peer_table.insert().values(s21_nickname=peer_nick)
                    result = session.execute(new_peer)
                    session.commit()
                    peer_id_temp = result.inserted_primary_key[0]

                cluster_id = session.execute(select(cluster_table.c.id).where(cluster_table.c.name == peer_cluster)).scalar()

                session_record = session.execute(select(session_table).where(session_table.c.peer_id == peer_id_temp)).fetchone()

                if session_record:
                    session.execute(
                        update(session_table).
                        where(session_table.c.peer_id == peer_id_temp).
                        values(online=True, cluster_id=cluster_id, row=peer_row, place=peer_place, timestamp=current_time)
                    )
                else:
                    new_session = session_table.insert().values(
                        peer_id=peer_id_temp, online=True, cluster_id=cluster_id, row=peer_row, place=peer_place, timestamp=func.now()
                    )

                    session.execute(new_session)

                session.commit()

    except Exception as ex:
        print(ex)

    finally:
        pass


if __name__ == "__main__":
    # create_all_tables()
    # create_all_kzn_clusters()
    update_peers_sessions({("jenniff", "va", 'g', 1),("diamondp", "et", 'f', 2)})