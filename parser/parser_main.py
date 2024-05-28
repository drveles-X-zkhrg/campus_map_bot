from parse_edu import *
from parser_sender import *

if __name__ == "__main__":
    temp_data = login_and_parse_campus_map()
    temp_json = convert_to_json(temp_data)
    update_peers(temp_json)
