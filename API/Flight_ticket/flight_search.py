import requests
from datetime import datetime

class FlightSearch:
    def __init__(self):
        self.SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
        self.SEARCH_API_KEY = "MxIBZFGvcU2vQ7zj8V3Zz-nv7Zwonn69"
        self.today = datetime.now().strftime("%d/%/%Y")
        self.SEARCH_PARA = {
            "fly_from": "",
            "date_from": self.today,
            "date_to": "07/12/2022"
        }

        self.response = requests.get(url=self.SEARCH_ENDPOINT, params=self.SEARCH_PARA, headers=self.SEARCH_API_KEY)
