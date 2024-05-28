from .bot_models_db import *
from .bot_engine_db import *


def create_all_tables():
    metadata_objs.create_all(engine)


def drop_all_tables():
    metadata_objs.drop_all(engine)


def create_all_kzn_clusters():
    """
    ## Initializating clusters for KZN campus.
    It is executed once, immediately after creating the tables.
    """
    try:
        with Session() as session:
            cluster_names = ["et", "ev", "si", "ge", "pr", "un", "va"]
            for cluster_name in cluster_names:
                existing_cluster = session.execute(
                    sqlalchemy.select(cluster_table.c.id).where(
                        cluster_table.c.name == cluster_name
                    )
                ).fetchone()

                if not existing_cluster:
                    cluster = cluster_table.insert().values(name=cluster_name)
                    session.execute(cluster)

            session.commit()

    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    create_all_tables()
