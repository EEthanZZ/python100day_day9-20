import requests
from twilio.rest import Client

MY_API_KEY = "5b3d56f17ad033dc4198740bc0c89ba9"
MY_LAT = -37.832642
MY_LNG = 145.125031
PART = "current,daily,minutely"
OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

TWILIO_SID = "AC185eb2acbcdee217a8e18b6a364a56bf"
TWILIO_AUTH_TOKEN = "84b5b2e3595ce29205c2a3b7b6660377"
TWILIO_NUM = "+16614864166"

# connection = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall?lat={MY_LAT}&lon={MY_LNG}"
#                               f"&exclude={PART}&appid={MY_API_KEY}")
# weather = connection.json()
# print(weather)

weather_param = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": MY_API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWN_ENDPOINT, params=weather_param)
weather_data = response.json()
print(weather_data)

# for i in range(0, 12):
#     hourly12_weather = weather_data["hourly"][i]["weather"][0]["id"]
#     print(hourly12_weather)
# print()
# print()

will_rain = False
weather = weather_data["hourly"][0:12]
for hourly_weather in weather:
    code = hourly_weather["weather"][0]["id"]
    if code < 700:
        will_rain = True

if will_rain:
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages \
        .create(
        body="bring an umbrella with you",
        from_=TWILIO_NUM,
        to="+61404346835"
    )
else:
    print("no umbrella")
