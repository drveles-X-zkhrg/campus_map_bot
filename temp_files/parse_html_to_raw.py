def parse_raw_from_cluster_htmls(cluster_name):
    """
    This func parse raw data from cluster html files 

    Return:
    peers {(nick, cluster_name, row_char, row_int)}
    """
    import re

    peers = set()
    with open(f"temp_files/{cluster_name}.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    profile_pattern = re.compile(r"profile/(\w+)@")
    profiles = profile_pattern.finditer(html_content)

    for match in profiles:
        start_pos = match.start()
        end_pos = match.end()

        left_part = html_content[:start_pos]
        left_part = "".join(reversed(left_part))
        letter_match = re.search(r"<([a-z])>", left_part)
        if letter_match:
            row_letter = letter_match.group(0)[::-1][1]
        else:
            row_letter = None

        right_part = html_content[end_pos:]
        number_match = re.search(r">(\d)<", right_part)
        if number_match:
            row_number = number_match.group(0)[1]
        else:
            row_number = None

        peers.add((match.group(1),cluster_name, row_letter, row_number))
    for peer in peers:
        print(peer)

    print(len(peers))

if __name__ == "__main__":
    parse_raw_from_cluster_htmls("et")
