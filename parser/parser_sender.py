"""
## Sending json to DB API
"""

import os
import logging
import requests


def update_peers(data_in_json: dict):
    """
    ## Sending parsed data to redis API
    """

    api_address = os.getenv("API_ADDRESS", "localhost")
    api_port = os.getenv("API_PORT", ":8000")
    url_to_api = f"{api_address}{api_port}/update_peers/"
    headers = {"Content-Type": "application/json", "Sender": "update_peers()"}

    try:
        response = requests.post(
            url=url_to_api,
            json=data_in_json,
            headers=headers,
            timeout=5,
        )
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        logging.error("An error occurred: %s", e)
