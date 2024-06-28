"""
## Tests for parser service
"""

import logging
from parse_edu import login_and_parse_campus_map
from parse_raw_from_html import convert_to_json
from parser_sender import update_peers

def test_conn_parser_to_api():
    """
    Test connecion to API service
    """
    test_data = {("jenniff", "va", "f", 3)}
    logging.info("test data to convert: %s", test_data)
    test_json = convert_to_json(test_data)
    logging.info("converted to test json: %s", test_json)
    update_peers(test_json)
    logging.info("sended to api ?")

if __name__ == "__main__":
    test_conn_parser_to_api()
