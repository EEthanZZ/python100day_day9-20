import requests
from datetime import datetime

SEARCH_ENDPOINT = "https://tequila-api.kiwi.com"
SEARCH_API_KEY = "MxIBZFGvcU2vQ7zj8V3Zz-nv7Zwonn69"
class FlightSearch:
    def get_dest_code(self, city_name):
        location_endpoint = f"{SEARCH_ENDPOINT}/locations/query"
        headers = {
            "apikey": SEARCH_API_KEY
        }
        query = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(
            url=location_endpoint,
            headers=headers,
            params=query
        )
        result = response.json()["locations"]
        code = result[0]["code"]
        return code
