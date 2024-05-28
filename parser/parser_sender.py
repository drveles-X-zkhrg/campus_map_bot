import requests


def update_peers(data_in_json):
    """
    ## Sending parsed data to redis API
    """

    url_to_redis_api = "https://redis_api_url"
    headers = {"Content-Type": "application/json", "Sender": "update_peers()"}

    try:
        response = requests.post(
            url=url_to_redis_api,
            json=data_in_json,  # используем json вместо data
            headers=headers,
        )
        response.raise_for_status()  # проверка на успешность запроса
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
