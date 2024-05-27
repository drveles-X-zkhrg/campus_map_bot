from parser.parse_edu import *
from baza.bot_models_db import *
from baza.bot_update_db import update_peers_sessions

if __name__ == "__main__":
    temp_data = login_and_parse_campus_map()
    
    start_time = time.time()

    update_peers_sessions(temp_data)

    print("updated db on ", time.time() - start_time)


