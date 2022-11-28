import requests
from datetime import datetime

MY_LAT = -37.843763
MY_LNG = 145.149133

parameters = {"lat": MY_LAT,
              "lng": MY_LNG,
              "formatted": 0}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
sunset_hour = int(sunset.split("T")[1].split(":")[0])

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
iss_lat = float(data["iss_position"]["latitude"])
iss_lng = float(data["iss_position"]["longitude"])
print(iss_lng)
time_now = datetime.now()

print(data)
print(sunrise)
print(sunset)
print(time_now)
print(sunrise_hour)
print(sunset_hour)
print(time_now.hour)



