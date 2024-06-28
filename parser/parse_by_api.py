"""
## Using School 21 API to get peers data.
"""

import os
import requests


def get_token():
    """
    ###  Auth and return token: `Bearer $token`
    """
    request = requests.post(
        url="https://auth.sberclass.ru/auth/realms/EduPowerKeycloak/protocol/openid-connect/token",
        data={
            "username": os.getenv("EDU_SCHOOL_LOGIN"),
            "password": os.getenv("EDU_SCHOOL_PASSWORD"),
            "grant_type": "password",
            "client_id": "s21-open-api",
        },
    )

    # requests.post()
    print(request)
    # print(request.json())

    token = request.json()["access_token"]

    token = "Bearer " + token
    return token


def parse():
    """
    ### Getting info about peers on campuses maps
    """
    token = get_token()

    request = requests.get(
        url="https://edu-api.21-school.ru/services/21-school/api/v1/campuses",
        headers={"accept": "application/json", "Authorization": token},
    )
    print(request)
    print(request.json())


if __name__ == "__main__":

    parse()
