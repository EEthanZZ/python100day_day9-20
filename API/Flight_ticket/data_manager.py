import requests
from pprint import pprint

SHEETY_ENDPOINT = "https://api.sheety.co/a581b08495e47520093ca6826d9aa89c/flightDealsCopy/prices"


class DataManager:
    def __init__(self):
        self.des_data = {}

    def get_dest(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.des_data = data["prices"]
        pprint(self.des_data)


DataManager.get_dest(DataManager)
