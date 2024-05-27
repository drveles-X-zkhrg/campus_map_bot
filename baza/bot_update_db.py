from sqlalchemy import select, update, func
from .bot_models_db import *
from .bot_initialize_db import *


def all_peers_offline():
    """
    ## This func turned off column sessions.online
    """
    try:
        # Создаем выражение SQL для обновления значений
        update_statement = update(session_table).values(online=False)

        # Выполняем запрос
        with engine.connect() as conn:
            conn.execute(update_statement)
            conn.commit()

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
        with Session() as session:
            all_peers_offline()

            for peer_nick, peer_cluster, peer_row, peer_place in peers_sessions:
                s21_peer = session.execute(
                    select(s21_peer_table.c.id).where(
                        s21_peer_table.c.s21_nickname == peer_nick
                    )
                ).fetchone()
                if s21_peer:
                    peer_id_temp = s21_peer[0]
                else:
                    new_peer = s21_peer_table.insert().values(s21_nickname=peer_nick)
                    result = session.execute(new_peer)
                    session.commit()
                    peer_id_temp = result.inserted_primary_key[0]

                cluster_id = session.execute(
                    select(cluster_table.c.id).where(
                        cluster_table.c.name == peer_cluster
                    )
                ).scalar()

                session_record = session.execute(
                    select(session_table).where(session_table.c.peer_id == peer_id_temp)
                ).fetchone()

                if session_record:
                    session.execute(
                        update(session_table)
                        .where(session_table.c.peer_id == peer_id_temp)
                        .values(
                            online=True,
                            cluster_id=cluster_id,
                            row=peer_row,
                            place=peer_place,
                            timestamp=func.now(),
                        )
                    )
                else:
                    new_session = session_table.insert().values(
                        peer_id=peer_id_temp,
                        online=True,
                        cluster_id=cluster_id,
                        row=peer_row,
                        place=peer_place,
                        timestamp=func.now(),
                    )

                    session.execute(new_session)
                session.commit()

    except Exception as ex:
        print(ex)

    finally:
        pass


if __name__ == "__main__":
    update_peers_sessions({("testing", "va", "a", 1)})
