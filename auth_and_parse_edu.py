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
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import time, re


def parse_raw_data_from_cluster(cluster_name, cluster_data) -> set:
    """
    ### This func parse raw data from clustests data

    Return:
    `peers in cluster:` {(nick, cluster_name, row_char, row_int), ...}
    """

    peers = set()
    profile_pattern = re.compile(r"profile/(\w+)@")
    profiles = profile_pattern.finditer(cluster_data)

    for match in profiles:
        start_pos = match.start()
        end_pos = match.end()

        left_part = cluster_data[:start_pos]
        left_part = "".join(reversed(left_part))
        letter_match = re.search(r"<([a-z])>", left_part)
        if letter_match:
            row_letter = letter_match.group(0)[::-1][1]
        else:
            row_letter = None

        right_part = cluster_data[end_pos:]
        number_match = re.search(r">(\d)<", right_part)
        if number_match:
            row_number = number_match.group(0)[1]
        else:
            row_number = None

        peers.add((match.group(1), cluster_name, row_letter, row_number))

    # temp print to visualisate
    for peer in peers:
        print(peer)
    print(f"in {cluster_name} placed {len(peers)} at {time.ctime()}")

    return peers


def login_and_parse_campus_map():
    all_peers = set()
    clusters_xpaths_dct = {
        "et": '//*[@id="root"]/div[2]/div/div[2]/div[1]/div[2]/div/div/ul/li[1]',
        "ev": '//*[@id="root"]/div[2]/div/div[2]/div[1]/div[2]/div/div/ul/li[2]',
        "si": '//*[@id="root"]/div[2]/div/div[2]/div[1]/div[2]/div/div/ul/li[3]',
        "ge": '//*[@id="root"]/div[2]/div/div[2]/div[2]/div[2]/div/div/ul/li[1]',
        "pr": '//*[@id="root"]/div[2]/div/div[2]/div[2]/div[2]/div/div/ul/li[2]',
        "un": "/html/body/div/div[2]/div/div[2]/div[2]/div[2]/div/div/ul/li[3]",
        "va": "/html/body/div/div[2]/div/div[2]/div[2]/div[2]/div/div/ul/li[4]",
    }
    
    chromedriver_path = './chromedriver'
    chrome_service = Service(chromedriver_path)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--remote-debugging-port=9222")

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

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
        # finish open site

        # showing hidden (collapsed) floors
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

        for cluster_name in clusters_xpaths_dct:
            print(f"start parse {cluster_name}")
            cluster_xpath = clusters_xpaths_dct[cluster_name]
            driver.find_element(By.XPATH, cluster_xpath).click()
            time.sleep(3.5)
            html = driver.find_element(By.TAG_NAME, "body").get_attribute("innerHTML")
            peers_from_this_cluster = parse_raw_data_from_cluster(cluster_name, html)
            if not peers_from_this_cluster:
                print(f"\033[91m cluster {cluster_name} empty or failed load cluster data \033[0m")
            all_peers.update(peers_from_this_cluster)
        
        print(f"\nPeers counter from all clusters {len(all_peers)}\n")

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()


def time_test_parse():
    start = time.time()
    login_and_parse_campus_map()
    print(f"parse take {time.time() - start} seconds")


if __name__ == "__main__":

    # login_and_parse_campus_map()
    time_test_parse()
