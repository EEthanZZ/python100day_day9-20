from datetime import datetime, timedelta

from data_manager import DataManager
data_manager = DataManager()
sheet_data = data_manager.get_dest()
from flight_search import FlightSearch
search = FlightSearch()
from notification_manager import NotificationManager
notification_manager = NotificationManager()


tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
today_after_60days = (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y")
ORIGINAL_CITY = "LON"
print(tomorrow)
print(sheet_data)
if sheet_data[0]["iataCode"] == "":
    for i in sheet_data:
        i["itatCode"] = search.get_dest_code(i["city"])
    sheet_data = data_manager.get_dest()
    data_manager.get_dest_code()

    for des in sheet_data:
        flight = search.flight_ticket(
            dept_ct_code=ORIGINAL_CITY,
            dest_ct_code=des["iataCode"],
            from_time=tomorrow,
            to_time=today_after_60days
        )
    if flight.price < des["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )


