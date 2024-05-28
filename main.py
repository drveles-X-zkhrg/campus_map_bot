"""
Entry point to parse and update db
"""
from parser.parse_edu import *
from sql_db.bot_models_db import *
from sql_db.bot_update_db import update_peers_sessions

if __name__ == "__main__":
    # full_time_parse_and_db()
    update_peers_sessions(login_and_parse_campus_map())

