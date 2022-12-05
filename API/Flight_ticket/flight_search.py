import requests
from datetime import datetime

SEARCH_ENDPOINT = "https://tequila-api.kiwi.com"
SEARCH_API_KEY = "MxIBZFGvcU2vQ7zj8V3Zz-nv7Zwonn69"
class FlightSearch:
    def get_dest_code(self, city_name):
        code = "Testing"
        return code