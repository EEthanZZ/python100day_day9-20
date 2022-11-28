import requests
from datetime import datetime
import time
import smtplib

MY_LAT = -37.843763
MY_LNG = 145.149133
MY_EMail = "zycc2727@gmail.com"
PASSWORD = "wcbujxxyjdbnmjdl"


def is_night():
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
    time_now = datetime.now().hour

    if time_now >= sunset_hour or time_now <= sunrise_hour:
        return True


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_lat = float(data["iss_position"]["latitude"])
    iss_lng = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LNG - 5 <= iss_lng <= MY_LNG + 5:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMail, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMail, to_addrs="yczhu@yahoo.com",
                                msg=f"Subject:Look Up\n\nLook Up now")
