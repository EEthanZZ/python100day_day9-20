import requests

class DataManager:
    def __init__(self):
        self.SHEETY_ENDPOINT = "https://api.sheety.co/a581b08495e47520093ca6826d9aa89c/flightDealsCopy/prices"
        self.SHEETY_PARA = {
            "prices": {
                "city": "city",
                "IATA Code": "IATA Code",
                "Lowest Price": "Lowest Price"
            }
        }

        self.response = requests.post(url=self.SHEETY_ENDPOINT, json=self.SHEETY_PARA)

