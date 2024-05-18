from dotenv import dotenv_values

"""
Gettin login and pass from .env file to edu.21-school.ru
File format:
    LOGIN=login
    PASSWORD=pass
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, requests


def login_and_parce_campus_map():

    driver = webdriver.Chrome()
    driver.scopes = [".*"]
    try:
        driver.get("https://edu.21-school.ru/campus")
        login_field = driver.find_element(By.NAME, "username")
        login_field.send_keys(dotenv_values(".env").get("LOGIN"))
        time.sleep(0.5)
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys(dotenv_values(".env").get("PASSWORD"))
        time.sleep(0.5)
        password_field.send_keys(Keys.ENTER)
        time.sleep(4)
        # finish open site

        floor2_table = driver.find_element(
            By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div[1]/div[2]'
        )
        floor3_table = driver.find_element(
            By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div[2]/div[2]'
        )

        # showing hidden (collapsed) floors
        if not floor2_table.is_displayed():
            driver.find_element(
                By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div[1]/div[1]/button/div'
            ).click()  # Floor 2
            time.sleep(1)
        if not floor3_table.is_displayed():
            driver.find_element(
                By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div[2]/div[1]/button/div'
            ).click()  # Floor 3
            time.sleep(1)

        driver.find_element(
            By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div[1]/div[2]/div/div/ul/li[1]'
        ).click()  # Eternity
        time.sleep(4)
        body_content = driver.find_element(By.TAG_NAME, "body").get_attribute(
            "innerHTML"
        )
        with open("temp_files/et.html", "w", encoding="utf-8") as file:
            file.write(body_content)
        driver.find_element(
            By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div[1]/div[2]/div/div/ul/li[2]'
        ).click()  # Evolution
        time.sleep(5)
        body_content = driver.find_element(By.TAG_NAME, "body").get_attribute(
            "innerHTML"
        )
        with open("temp_files/ev.html", "w", encoding="utf-8") as file:
            file.write(body_content)
        driver.find_element(
            By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div[1]/div[2]/div/div/ul/li[3]'
        ).click()  # Singularity
        time.sleep(4)
        body_content = driver.find_element(By.TAG_NAME, "body").get_attribute(
            "innerHTML"
        )
        with open("temp_files/si.html", "w", encoding="utf-8") as file:
            file.write(body_content)
        driver.find_element(
            By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div[2]/div[2]/div/div/ul/li[1]'
        ).click()  # Genome
        time.sleep(4)
        body_content = driver.find_element(By.TAG_NAME, "body").get_attribute(
            "innerHTML"
        )
        with open("temp_files/ge.html", "w", encoding="utf-8") as file:
            file.write(body_content)
        driver.find_element(
            By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div[2]/div[2]/div/div/ul/li[2]'
        ).click()  # Progress
        time.sleep(4)
        body_content = driver.find_element(By.TAG_NAME, "body").get_attribute(
            "innerHTML"
        )
        with open("temp_files/pr.html", "w", encoding="utf-8") as file:
            file.write(body_content)
        driver.find_element(
            By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div[2]/div/div/ul/li[3]"
        ).click()  # Universe
        time.sleep(5)
        body_content = driver.find_element(By.TAG_NAME, "body").get_attribute(
            "innerHTML"
        )
        with open("temp_files/un.html", "w", encoding="utf-8") as file:
            file.write(body_content)
        driver.find_element(
            By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div[2]/div/div/ul/li[4]"
        ).click()  # Vault
        time.sleep(3)
        body_content = driver.find_element(By.TAG_NAME, "body").get_attribute(
            "innerHTML"
        )
        with open("temp_files/va.html", "w", encoding="utf-8") as file:
            file.write(body_content)

        time.sleep(20)

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()


def main():
    login_and_parce_campus_map()


if __name__ == "__main__":
    main()
