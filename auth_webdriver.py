import time, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv, dotenv_values


def loging_dotenv():
    '''
    Gettin login and pass from .env file to edu.21-school.ru
    
    File format: 
        LOGIN={login}
        PASSWORD={pass}
    '''

    dotenv_path = os.path.join(".env")
    load_dotenv(dotenv_path)


def main():
    loging_dotenv()
    user_login = dotenv_values(".env").get("LOGIN")
    user_pass = dotenv_values(".env").get("PASSWORD")

    driver = webdriver.Chrome()
    driver.get("https://edu.21-school.ru/")
    login_field = driver.find_element(By.NAME, "username")
    login_field.send_keys(user_login)
    pasword_field = driver.find_element(By.NAME, "password")
    pasword_field.send_keys(user_pass)
    driver.find_element(By.XPATH, '//*[@id="login"]/div/div/div[2]/div/div/form/div[3]/button').click()
    driver.get("https://edu.21-school.ru/campus") 


    print(login_field)

    time.sleep(10)
    


if __name__ == "__main__":
    main()
