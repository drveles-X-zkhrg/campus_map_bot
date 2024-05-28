from dotenv import dotenv_values

"""
Gettin login and pass from .env file to edu.21-school.ru
File format:
    LOGIN=login
    PASSWORD=pass
"""
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from parse_raw_from_html import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def create_chromedriver():
    chromedriver_path = "./venv/chromedriver"
    chrome_service = Service(chromedriver_path)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("window-size=1200x1040")

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return driver


def auth_edu(driver):
    """
    Log in to the edu website
    """
    try:
        driver.get("https://edu.21-school.ru/campus")
        login_field = driver.find_element(By.NAME, "username")
        login_field.send_keys(dotenv_values(".env").get("LOGIN"))
        time.sleep(0.5)
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys(dotenv_values(".env").get("PASSWORD"))
        time.sleep(0.5)
        password_field.send_keys(Keys.ENTER)
        time.sleep(3)
    except Exception as ex:
        print(ex)


def displaying_floors(driver):
    """
    Unfolding the floor block
    """
    try:
        floor2_t = driver.find_element(
            By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div[1]/div[2]'
        )
        floor3_t = driver.find_element(
            By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div[2]/div[2]'
        )
        if not floor2_t.is_displayed():  # Floor 2
            driver.find_element(
                By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div[1]/div[1]/button/div'
            ).click()
            time.sleep(1)
        if not floor3_t.is_displayed():  # Floor 3
            driver.find_element(
                By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div[2]/div[1]/button/div'
            ).click()
            time.sleep(1)
    except Exception as ex:
        print(ex)


def parse_each_cluster(driver):
    """
    Open each cluster, and parse peers from html
    """

    all_peers = set()
    clusters_xpaths_dct = {
        "et": '//*[@id="root"]/div[2]/div/div[2]/div[1]/div[2]/div/div/ul/li[1]',
        "ev": '//*[@id="root"]/div[2]/div/div[2]/div[1]/div[2]/div/div/ul/li[2]',
        "si": '//*[@id="root"]/div[2]/div/div[2]/div[1]/div[2]/div/div/ul/li[3]',
        "ge": '//*[@id="root"]/div[2]/div/div[2]/div[2]/div[2]/div/div/ul/li[1]',
        "pr": '//*[@id="root"]/div[2]/div/div[2]/div[2]/div[2]/div/div/ul/li[2]',
        "un": '//*[@id="root"]/div[2]/div/div[2]/div[2]/div[2]/div/div/ul/li[3]',
        "va": '//*[@id="root"]/div[2]/div/div[2]/div[2]/div[2]/div/div/ul/li[4]',
    }
    try:

        for cluster_name in clusters_xpaths_dct:
            print(f"start parse {cluster_name}")
            cluster_xpath = clusters_xpaths_dct[cluster_name]
            driver.find_element(By.XPATH, cluster_xpath).click()
            time.sleep(4.5)
            html = driver.find_element(By.TAG_NAME, "body").get_attribute("innerHTML")
            peers_from_this_cluster = parse_raw_data_from_cluster(cluster_name, html)
            if not peers_from_this_cluster:
                print(
                    f"\033[91m cluster {cluster_name} empty or failed load cluster data \033[0m"
                )
            all_peers.update(peers_from_this_cluster)

        print(f"\nPeers counter from all clusters {len(all_peers)} at {time.ctime()}\n")

    except Exception as ex:
        print(ex)

    finally:
        return all_peers


def login_and_parse_campus_map():
    driver = create_chromedriver()

    auth_edu(driver)
    displaying_floors(driver)
    all_peers = parse_each_cluster(driver)

    driver.close()
    driver.quit()
    return all_peers


if __name__ == "__main__":
    login_and_parse_campus_map()
    # time_test_parse()
