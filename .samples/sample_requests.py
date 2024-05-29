import requests
import json
import re
from uuid import uuid4
from dotenv import dotenv_values


class LoginService:
    GRAPHQL_URL = "https://edu.21-school.ru/services/graphql"
    BASE_URL = "https://auth.sberclass.ru/auth/realms/EduPowerKeycloak"
    COOKIE_URL_TEMPLATE = (
        BASE_URL
        + "/protocol/openid-connect/auth?client_id=school21&redirect_uri=https://edu.21-school.ru/&state=%s&response_mode=fragment&response_type=code&scope=openid&nonce=%s"
    )
    TOKEN_URL = BASE_URL + "/protocol/openid-connect/token"

    def __init__(self, full_login, login, password):
        self.full_login = full_login
        self.login = login
        self.password = password
        self.school_id = None
        self.token = None

    def loginM(self):
        print("[Login] start")

        try:
            session = requests.Session()
            state = str(uuid4())
            nonce = str(uuid4())

            response = session.get(self.COOKIE_URL_TEMPLATE % (state, nonce))
            response_str = response.text

            login_action_match = re.search(r'https:.+?(?=")', response_str, re.MULTILINE)

            if login_action_match:
                url = login_action_match.group(0).replace("amp;", "")
            else:
                print("[Login] loginAction error")
                return False

            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            data = {"username": self.full_login, "password": self.password}
            response = session.post(url, data=data, headers=headers)

            location = response.headers.get("location")
            if location:
                response = session.post(location)
            else:
                print("[Login] location1 error")
                return False

            location = response.headers.get("location")
            if location:
                response = session.post(location)
            else:
                print("[Login] location2 error")
                return False

            response_str = response.headers.get("location")
            o_auth_code_match = re.search("(?<=code=).+", response_str, re.MULTILINE)
            if o_auth_code_match:
                o_auth_code = o_auth_code_match.group(0)
            else:
                print("[Login] oAuthCode error")
                return False

            data = {
                "client_id": "school21",
                "code": o_auth_code,
                "grant_type": "authorization_code",
                "redirect_uri": "https://edu.21-school.ru/",
            }
            response = session.post(self.TOKEN_URL, data=data, headers=headers)

            response_json = json.loads(response.text)
            self.token = response_json.get("access_token").replace('"', "")

            # Assuming sendRequest method is implemented similarly
            json_node = self.send_request(request_body="your_request_body_here")

            self.school_id = (
                json_node.get("user").get("user_school_roles")[0].get("school_id")
            )
            print("[Login] token " + self.token + "\nschoolId " + self.school_id)
            return True
        except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
            print("[Login] token error " + str(e))
            return False

    def send_request(self, request_body):
        headers = {
            "Authorization": "Bearer " + self.token,
            "schoolId": self.school_id,
            "Content-Type": "application/json",
        }
        try:
            response = requests.post(
                self.GRAPHQL_URL, data=request_body, headers=headers
            )
            response_json = json.loads(response.text)
            return response_json.get("data")
        except requests.exceptions.RequestException as e:
            print("[PARSER] ERROR " + str(e))
            return None


if __name__ == "__main__":
    ls = LoginService(
        dotenv_values(".env").get("LOGIN"),
        "jenniffr",
        dotenv_values(".env").get("PASSWORD"),
    )
    ls.loginM()

