"""
## Using AUTH 2.0 to getting token to edu platform
"""

import logging
import os
import time
import requests

_TOKEN_CACHE = {"token": None, "expiry": 0.0}


def get_token():
    """
    ###  Auth and return token: `Bearer $token`
    """

    if _TOKEN_CACHE["token"] and time.time() < _TOKEN_CACHE["expiry"]:
        return _TOKEN_CACHE["token"]

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

    token_response = request.json()
    access_token = token_response.get("access_token", "")

    _TOKEN_CACHE["token"] = "Bearer " + access_token

    expires_in = token_response.get("expires_in", 3600)
    _TOKEN_CACHE["expiry"] = time.time() + expires_in - 60

    logging.info(
        "New OAuth token received and cached. It will expire in %d seconds.", expires_in
    )

    return _TOKEN_CACHE["token"]
