import re

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

    # here heed logging to
    print(f"{len(peers)} peers in {cluster_name}")

    return peers
