"""
## Using AUTH 2.0 to getting token to edu platform
"""

import logging
import os
import time
import requests

_cached_token = None
_token_expiry = 0


def get_token():
    """
    ###  Auth and return token: `Bearer $token`
    """

    global _cached_token, _token_expiry

    if _cached_token and time.time() < _token_expiry:
        return _cached_token

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

    _cached_token = "Bearer " + access_token

    expires_in = token_response.get("expires_in", 3600)
    _token_expiry = time.time() + expires_in - 60

    return _cached_token


def clear_token_cache():
    """Clean cache"""

    global _cached_token, _token_expiry
    _cached_token = None
    _token_expiry = 0
