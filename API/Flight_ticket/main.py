from data_manager import DataManager
data_manager = DataManager()
sheet_data = data_manager.get_dest()

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for i in sheet_data:
        i["iataCode"] = flight_search.get_dest_code(i["city"])
    print(f"{sheet_data}")