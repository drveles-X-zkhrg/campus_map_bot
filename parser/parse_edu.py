"""
## Logining and parse school edu site.
"""

import os
import time
import sys
import logging
from dotenv import load_dotenv

from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
)
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from parse_raw_from_html import parse_raw_data_from_cluster

logging.basicConfig(level=logging.WARN, stream=sys.stdout)


def create_chromedriver():
    """
    ### Create driver for browser
    """
    chromedriver_path = "./chromedriver"
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
    ### Log in to the edu website
    """
    try:
        driver.get("https://edu.21-school.ru/campus")
        load_dotenv()
        login_field = driver.find_element(By.NAME, "username")
        login_field.send_keys(os.getenv("EDU_SCHOOL_LOGIN"))
        time.sleep(0.5)
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys(os.getenv("EDU_SCHOOL_PASSWORD"))
        time.sleep(0.5)
        password_field.send_keys(Keys.ENTER)
        time.sleep(3)
    except (NoSuchElementException, ElementNotInteractableException) as ex:
        logging.error("An error occurred while trying to display floors: %s", ex)


def displaying_floors(driver):
    """
    ### Unfolding the floor block
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
    except (NoSuchElementException, ElementNotInteractableException) as ex:
        logging.error("An error occurred while trying to display floors: %s", ex)


def parse_each_cluster(driver) -> set[tuple]:
    """
    ### Open each cluster, and parse peers from html
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
        for cluster_name, cluster_xpath in clusters_xpaths_dct.items():
            driver.find_element(By.XPATH, cluster_xpath).click()
            time.sleep(7)
            html = driver.find_element(By.TAG_NAME, "body").get_attribute("innerHTML")
            peers_from_this_cluster = parse_raw_data_from_cluster(cluster_name, html)
            if not peers_from_this_cluster:
                logging.warning(
                    "cluster %s empty or failed to load cluster data", cluster_name
                )
            all_peers.update(peers_from_this_cluster)
            logging.info("cluster %s parsed", cluster_name)

    except (NoSuchElementException, ElementNotInteractableException) as ex:
        logging.error("An error occurred while parsing clusters: %s", ex)

    return all_peers


def login_and_parse_campus_map() -> set[tuple]:
    """
    ### Entery point to parse edu
    """
    driver = create_chromedriver()
    logging.info("driver created")
    auth_edu(driver)
    logging.info("auth success")
    displaying_floors(driver)
    logging.info("disp floors success")
    all_peers = parse_each_cluster(driver)
    logging.info("parse clusters success")

    driver.close()
    driver.quit()
    return all_peers


if __name__ == "__main__":
    login_and_parse_campus_map()
