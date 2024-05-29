import re, json
from datetime import datetime


def parse_raw_data_from_cluster(cluster_name, cluster_data) -> set:
    """
    ### This func parse peers info from clustests data

    Return:
    `peers in cluster:` {(nick, cluster_name, row_char, row_int), ...}
    """

    peers = set()
    profile_pattern = re.compile(r"profile/(\w+)@")
    profiles = profile_pattern.finditer(cluster_data)

    for match in profiles:
        start_pos = match.start()
        end_pos = match.end()

        left_part = cluster_data[:start_pos]
        left_part = "".join(reversed(left_part))
        letter_match = re.search(r"<([a-z])>", left_part)
        if letter_match:
            row_letter = letter_match.group(0)[::-1][1]
        else:
            row_letter = None

        right_part = cluster_data[end_pos:]
        number_match = re.search(r">(\d)<", right_part)
        if number_match:
            row_number = number_match.group(0)[1]
        else:
            row_number = None

        peers.add((match.group(1), cluster_name, row_letter, row_number))

    # here heed logging to log file
    print(f"{len(peers)} peers in {cluster_name}")

    return peers


def convert_to_json(parsed_data: set[tuple]):
    """
    Convert a set of tuples to JSON.
    "peers": {
                "s21_peer_nick": {
                        "status": "val"
                        "cluster": "val",
                        "row": "val",
                        "col": "val",
                        "time": "val",
                },
    """
    # if not isinstance(parsed_data, set) or not len(parsed_data):
    #     return None
    data_as_dict = {"peers": {}}

    for parsed_nick, parsed_cluster, parsed_row, parsed_col in parsed_data:
        temp_peer_dict = {
            parsed_nick: {
                "status": "1",
                "cluster": parsed_cluster,
                "row": parsed_row,
                "col": parsed_col,
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        }

        data_as_dict["peers"].update(temp_peer_dict)

    json_parsed_data = json.dumps(data_as_dict)

    return json_parsed_data
