import requests
import pprint
import time


def test_requests():
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    payload = {"username": "jenniffr@student.21-school.ru", "password": "b"}
    headers = {
        "User-Agent": user_agent,
    }
    with requests.Session() as session:
        response = session.get("https://edu.21-school.ru/", headers=headers, auth=("jenniffr@student.21-school.ru", "a"))

        print(response.url)
        print(response.status_code)
        response = session.get("https://edu.21-school.ru/")
        print(response.url)
        print(response.status_code)


def main():
    test_requests()


if __name__ == "__main__":
    main()
