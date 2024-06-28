"""
## Using School 21 API to get peers data.
"""

import logging
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

    token = get_auth_token.get_token()
    for cluster_id, cluster_name in kzn_clusters.items():
        request = requests.get(
            url=f"https://edu-api.21-school.ru/services/21-school/api/v1/clusters/{cluster_id}/map?limit=101&offset=0&occupied=true",
            headers={"accept": "application/json", "Authorization": token},
            timeout=5,
        )

        print(request)
        print(request.json())


if __name__ == "__main__":

    parse_clusters()
