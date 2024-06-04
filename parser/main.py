"""
# Entery point to parse service
## Parse and send data to DB API
"""
import sys
import logging
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
)
from parse_edu import login_and_parse_campus_map
from parse_raw_from_html import convert_to_json
from parser_sender import update_peers

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

if __name__ == "__main__":
    while True:
        try:
            temp_data = login_and_parse_campus_map()
            logging.info("All cluster parsed")
            temp_json = convert_to_json(temp_data)
            logging.info("All converted parsed")
            update_peers(temp_json)
            logging.info("All data from parser sended")
            print("All data from parser sended")
        except (NoSuchElementException, ElementNotInteractableException) as all_ex:
            print("Parse failed, starting next try.")
            logging.error("Parse failed, starting next try. ERROR: %s", all_ex)
        finally:
            continue
