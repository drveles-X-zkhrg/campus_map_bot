"""
An attempt to make authorization through a request, but it does not work
"""

import requests, time, os
from dotenv import dotenv_values



def test_requests():
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"  # iMac
    user_login = dotenv_values(".env").get("LOGIN")
    user_pass = dotenv_values(".env").get("PASSWORD")
    address_nonce = "0943e87d-184e-4dbe-910a-8e39096fc387"
    address_state = "70d05990-2443-469e-8d7d-9fa65fe2fbb5"
    baze_address = "https://auth.sberclass.ru/auth/realms/EduPowerKeycloak"
    cookie_address = f"{baze_address}/protocol/openid-connect/auth?client_id=school21&redirect_uri=https%3A%2F%2Fedu.21-school.ru%2F&state={address_state}&response_mode=fragment&response_type=code&scope=openid&nonce={address_nonce}"
    tocken_address = f"{baze_address}/protocol/openid-connect/token"
    raw_token = ""
    form_data = {
        "code": raw_token,
        "grant_type": "authorization_code",
        "client_id": "school21",
        "redirect_uri": "https://edu.21-school.ru/",
    }

    with requests.Session() as session:
        cookie_response = session.get(
            url=cookie_address,
            auth=(
                user_login,
                user_pass,
            ),
        )  # cookie_request

        print(cookie_response.status_code)
        if cookie_response.status_code < 300:
            print(cookie_response.cookies)
            print("\n cookie_response success")

            """
            Here need parce cookies to raw token
            """
            time.sleep(5)

            response = session.post(
                url=tocken_address,
                data=form_data,
                cookies=cookie_response.cookies,
            )
            print(response.status_code)
            print(response.text)

