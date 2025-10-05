"""
## Using School 21 API to get peers data.
"""

import logging
from datetime import datetime, timedelta, timezone
import requests
import get_auth_token


def parse_clusters():
    """
    ### Getting info about online peers on campuses maps
    """
    kzn_clusters = {
        "34734": "et",
        "34735": "ev",
        "34736": "ge",
        "34737": "pr",
        "34738": "si",
        "34739": "un",
        "34740": "va",
    }
    all_peers = {"peers": {}}

    token = get_auth_token.get_token()
    url_endpoint = "https://platform.21-school.ru/services/21-school/api/v1/clusters/"

    for cluster_id, cluster_name in kzn_clusters.items():
        request = requests.get(
            url=f"{url_endpoint}{cluster_id}/map",
            params={"limit": "101", "offset": "0", "occupied": "true"},
            headers={"accept": "application/json", "Authorization": token},
            timeout=5,
        )
        if request.status_code > 200:
            logging.error("Failed parse cluster %s", cluster_name)
        else:
            moscow_time = datetime.now().astimezone(
                timezone(timedelta(hours=3), "Moscow")
            )
            moscow_time = moscow_time.strftime("%Y-%m-%d %H:%M:%S")

            for raw_peer in request.json()["clusterMap"]:
                clear_peer_data = {
                    "status": "1",
                    "cluster": cluster_name,
                    "row": raw_peer["row"],
                    "col": str(raw_peer["number"]),
                    "time": moscow_time,
                }
                all_peers["peers"][raw_peer["login"].split("@")[0]] = clear_peer_data

    print(all_peers)
    return all_peers


if __name__ == "__main__":

    parse_clusters()
