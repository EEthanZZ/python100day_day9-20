import requests
from datetime import datetime
parameters = {"lat": "51",
              "lng": "-0.12",
              "formatted": 0}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunset_hour = sunset.split("T")[1].split(":")[0]

time_now = datetime.now()

print(data)
print(sunrise)
print(sunset)
print(time_now)
print(sunrise_hour)
print(sunset_hour)
print(time_now.hour)



