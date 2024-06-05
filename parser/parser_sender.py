"""
## Sending json to DB API
"""
import os
import requests


def update_peers(data_in_json: dict):
    """
    ## Sending parsed data to redis API
    """

    API_ADDRESS = os.getenv("API_ADDRESS", "localhost")

    url_to_api = f"{API_ADDRESS}:8000"
    headers = {"Content-Type": "application/json", "Sender": "update_peers()"}

    try:
        response = requests.post(
            url=url_to_api,
            json=data_in_json,
            headers=headers,
            timeout=10,
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
