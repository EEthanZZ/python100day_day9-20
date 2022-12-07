import requests
from flight_data import FlightData

SEARCH_ENDPOINT = "https://api.tequila.kiwi.com"
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
        print(code)
        return code

    def flight_ticket(self, dept_ct_code, dest_ct_code, from_time, to_time):
        headers = {
            "apikey": SEARCH_API_KEY
        }
        query = {
            "fly_from": dept_ct_code,
            "fly_to": dest_ct_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "curr": "GBP",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
        }
        response = requests.get(url=f"{SEARCH_ENDPOINT}/v2/search",
                                params=query,
                                headers=headers)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {dest_ct_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            dept_city=data["route"][0]["cityFrom"],
            dept_air=data["route"][0]["flyFrom"],
            dest_air=data["route"][0]["flyTo"],
            dest_city=data["route"][0]["cityTo"],
            dept_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.dest_city}: £{flight_data.price}")
        return flight_data
