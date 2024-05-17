from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from dotenv import load_dotenv, dotenv_values
import os


def loging_dotenv():
    dotenv_path = os.path.join(".env")
    load_dotenv(dotenv_path)


def main():
    driver = webdriver.Chrome()
    driver.get("https://edu.21-school.ru/")
    loging_dotenv()
    login_field = driver.find_element(By.NAME, "username")
    login_field.send_keys(dotenv_values(".env").get("LOGIN"))
    pasword_field = driver.find_element(By.NAME, "password")
    pasword_field.send_keys(dotenv_values(".env").get("PASSWORD"))
    driver.find_element(By.XPATH, '//*[@id="login"]/div/div/div[2]/div/div/form/div[3]/button').click()
    driver.get("https://edu.21-school.ru/campus") 


    print(login_field)

    sleep(10)
    


if __name__ == "__main__":
    main()
