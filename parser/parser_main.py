"""
# Entery point to parse service
## Parse and send data to DB API
"""

import logging
from parse_edu import login_and_parse_campus_map
from parse_raw_from_html import convert_to_json
from parser_sender import update_peers
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
)

logging.basicConfig(level=logging.ERROR)

if __name__ == "__main__":
    while True:
        try:
            temp_data = login_and_parse_campus_map()
            temp_json = convert_to_json(temp_data)
            update_peers(temp_json)
        except (NoSuchElementException, ElementNotInteractableException) as all_ex:
            logging.error("Parse failed, starting next try")
        finally:
            continue
