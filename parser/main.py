"""
# Entery point to parse service
## Parse and send data to DB API
"""

import time
import parse_by_api
import parser_sender


if __name__ == "__main__":
    while True:

        all_peers = parse_by_api.parse_clusters()
        parser_sender.update_peers(all_peers)
        time.sleep(15)
