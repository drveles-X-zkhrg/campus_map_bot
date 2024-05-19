from dotenv import dotenv_values
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pickle
import time, os


def trying_get_cookies():
    """
    Gettin login and pass from .env file to edu.21-school.ru

    File format:
        LOGIN=login
        PASSWORD=pass
    """

    user_login = dotenv_values(".env").get("LOGIN")
    user_pass = dotenv_values(".env").get("PASSWORD")
    driver = webdriver.Chrome()

    try:
        driver.get("https://edu.21-school.ru/campus")
        login_field = driver.find_element(By.NAME, "username")
        login_field.send_keys(user_login)
        time.sleep(1)
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys(user_pass)
        time.sleep(1)
        password_field.send_keys(Keys.ENTER)
        time.sleep(6)
        # print(driver.get_cookie())
        pickle.dump(driver.get_cookies(), open(f"cookies", "wb"))

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()


def trying_login_with_cookies():
    driver = webdriver.Chrome()

    try:
        # driver.get("https://edu.21-school.ru/campus")

        # for cookie in driver.get_cookies():
        #     print(cookie)
        for cookie in pickle.load(open("cookies", "rb")):

            # cookie = {
            #     'domain': 'edu.21-school.ru',
            #     "httpOnly": False,
            #     "name": "tokenId",
            #     "path": "/",
            #     "sameSite": "Lax",
            #     "secure": False,
            #     "value": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ5V29landCTmxROWtQVEpFZnFpVzRrc181Mk1KTWkwUHl2RHNKNlgzdlFZIn0.eyJleHAiOjE3MTYwNjY2MzMsImlhdCI6MTcxNjAzMDYzMywiYXV0aF90aW1lIjoxNzE2MDMwNjMzLCJqdGkiOiJmYjUyMDUyYy1hMjU3LTRmOTQtODdiNy1kZWQyYmRiNzc1MWYiLCJpc3MiOiJodHRwczovL2F1dGguc2JlcmNsYXNzLnJ1L2F1dGgvcmVhbG1zL0VkdVBvd2VyS2V5Y2xvYWsiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiMmQ4ZWZmYjAtYWYxYy00NTQ4LWIxNmUtZDdiNzhmZjk0NWNjIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoic2Nob29sMjEiLCJub25jZSI6IjJmNjJiZjM2LWQ3ZWYtNDVkYS04OWUxLWQ5OTM2NzVkNTZlYyIsInNlc3Npb25fc3RhdGUiOiI5YWJlYzlkYy00MGFkLTQzZTAtOGFjOS02YTMyYTA3ZmJlMTMiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbImh0dHBzOi8vZWR1LjIxLXNjaG9vbC5ydSIsImh0dHBzOi8vZWR1LWFkbWluLjIxLXNjaG9vbC5ydSJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiZGVmYXVsdC1yb2xlcy1lZHVwb3dlcmtleWNsb2FrIiwib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwidXNlcl9pZCI6ImZmMzUxZGYxLTRiMjItNDM3My1iOTRiLWIyYmIxNTVhZGQ2YyIsIm5hbWUiOiJKZW5uaWZmZXIgUnViZW4iLCJhdXRoX3R5cGVfY29kZSI6ImRlZmF1bHQiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJqZW5uaWZmckBzdHVkZW50LjIxLXNjaG9vbC5ydSIsImdpdmVuX25hbWUiOiJKZW5uaWZmZXIiLCJmYW1pbHlfbmFtZSI6IlJ1YmVuIiwiZW1haWwiOiJqZW5uaWZmckBzdHVkZW50LjIxLXNjaG9vbC5ydSJ9.tvt_flha6mRBLGIN5iRVCxqU4uUS3hlWJMEKYMxs7icmS4EwgZifrGOX0XPxHuFkHXHFvrjDzYDq4OgHaqrcxAglE0QMhAmuHDnxoPWjzlnWSXarY-zl_E-z8K3Jn6AmIS9TFtoXNxg2cLSxHWj3UWjoYPBY75QclY9Rbmw4lY1Q_hqaqM76Y8Zh4-uz1rmQJ-IiFHUu9D6wGRTUVcnrjRO24PcGDnTLhIajFNAnqL1e_Bsqhx1zDSaTm8v01oZ7EA029E78pT9eLiHeY6rkx7cwrqmGJyHuROPnB5EEFC5wBFUCfHCR1Fl1I_8aM0oNsLAVRxfxfXEKbeTFf5-wKQ",
            # }
            print(cookie)
            driver.add_cookie(cookie)

        # driver.add_cookie({'domain': 'edu.21-school.ru', 'httpOnly': False, 'name': 'tokenId', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ5V29landCTmxROWtQVEpFZnFpVzRrc181Mk1KTWkwUHl2RHNKNlgzdlFZIn0.eyJleHAiOjE3MTYwNjc5MTIsImlhdCI6MTcxNjAzMTkxMywiYXV0aF90aW1lIjoxNzE2MDMxOTEyLCJqdGkiOiI1ODFjNDNkMi0yYWZhLTQwMGEtYjM1OC1iOWZkNjc3ZGJkNTAiLCJpc3MiOiJodHRwczovL2F1dGguc2JlcmNsYXNzLnJ1L2F1dGgvcmVhbG1zL0VkdVBvd2VyS2V5Y2xvYWsiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiMmQ4ZWZmYjAtYWYxYy00NTQ4LWIxNmUtZDdiNzhmZjk0NWNjIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoic2Nob29sMjEiLCJub25jZSI6ImRlOWZjYzU5LTNkNTMtNDdkNy04MTA3LTJlNzNhZDVhYmNhYyIsInNlc3Npb25fc3RhdGUiOiJjOTM5MjE1MS1hOTJhLTRiNTgtOGE3My1hYTg1MzkxNTU5YTUiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbImh0dHBzOi8vZWR1LjIxLXNjaG9vbC5ydSIsImh0dHBzOi8vZWR1LWFkbWluLjIxLXNjaG9vbC5ydSJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiZGVmYXVsdC1yb2xlcy1lZHVwb3dlcmtleWNsb2FrIiwib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwidXNlcl9pZCI6ImZmMzUxZGYxLTRiMjItNDM3My1iOTRiLWIyYmIxNTVhZGQ2YyIsIm5hbWUiOiJKZW5uaWZmZXIgUnViZW4iLCJhdXRoX3R5cGVfY29kZSI6ImRlZmF1bHQiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJqZW5uaWZmckBzdHVkZW50LjIxLXNjaG9vbC5ydSIsImdpdmVuX25hbWUiOiJKZW5uaWZmZXIiLCJmYW1pbHlfbmFtZSI6IlJ1YmVuIiwiZW1haWwiOiJqZW5uaWZmckBzdHVkZW50LjIxLXNjaG9vbC5ydSJ9.fUUXFiARGE5UNek4BBia-mlPYdUb9QCjGWhxxhAP8IKLaUxHNT7oCdsFGYkRDaCSCd6i36hcKeE6iq2Q70UF2Fbd2sC8bI-BKbr9NWMXB9BJiWJiWZGx1nYDeer4Ds0xqgi73ZaSAW3Zd7pgtoLTL8Sjf1JuSvxCgt8CEDwUiKdNwrE3o4NTCqbBwqzPIi-9VhQrfx3rFYv9luKzHaINgr4RKtJT1Ch_xgQmrEHyYI-myPSfYFyWdaHIryb87GEjR0k8LieiOAlAThzfGHqiyqG8XPJAKSRtog3gb5ioHhX7Ze14mlQ1caf1bXRwTgA02avIjtEiH0yim3iewzoSdA'})
        time.sleep(2)
        driver.get("https://edu.21-school.ru/campus")

        time.sleep(10)

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()


def main():
    # trying_get_cookies()
    trying_login_with_cookies()


if __name__ == "__main__":
    main()
