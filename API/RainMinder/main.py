import requests

MY_API_KEY = "5b3d56f17ad033dc4198740bc0c89ba9"
MY_LAT = -37.832642
MY_LNG = 145.125031
PART = "current,hourly"
OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"


connection = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall?lat={MY_LAT}&lon={MY_LNG}"
                              f"&exclude={PART}&appid={MY_API_KEY}")
weather = connection.json()
print(weather)

weather_param = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": MY_API_KEY
}

response = requests.get(OWN_ENDPOINT, params=weather_param)
print(response.json())