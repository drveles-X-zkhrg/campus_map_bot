"""
## Using AUTH 2.0 to getting token to edu platform
"""

import logging
import os
import requests


def get_token():
    """
    ###  Auth and return token: `Bearer $token`
    """
    request = requests.post(
        url="https://auth.21-school.ru/auth/realms/EduPowerKeycloak/protocol/openid-connect/token",
        data={
            "username": os.getenv("EDU_SCHOOL_LOGIN"),
            "password": os.getenv("EDU_SCHOOL_PASSWORD"),
            "grant_type": "password",
            "client_id": "s21-open-api",
        },
        timeout=5,
    )

    if request.status_code != 200:
        logging.error(
            "Failed to getting token! %d Error: %s", request.status_code, request.json()
        )

    token = "Bearer " + request.json().get("access_token", "")

    return token
