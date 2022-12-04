import requests
from datetime import datetime
import os
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
END_POINT = os.environ["END_POINT"]

SHEETY_END = os.environ["SHEETY_END"]


para = {"query": f"{input('what have you done?')}",
        }
headers = {"x-app-id": APP_ID,
           "x-app-key": API_KEY}
today = datetime.today().strftime("%Y/%m/%d")
time = datetime.today().strftime("%X")
print(today)
nut_post = requests.post(url=END_POINT, json=para, headers=headers)
result = nut_post.json()
print(result)
a = [v for (k, v) in result.items()]
exercise = str(a[0][0]['name']).title()
dura_time = str(a[0][0]['duration_min'])
calo = str(a[0][0]['nf_calories'])

sheeety_para = {
    "workout": {
        "date": today,
        "time": time,
        "exercise": exercise,
        "calories": calo

    }
}
bearer_auth = os.environ["bearer_auth"]
sheet_auth = {"Authorization": f"Bearer {bearer_auth}"}
sheet_response = requests.post(SHEETY_END, json=sheeety_para, headers=sheet_auth)
print(sheet_response.text)
print(os.environ.get("SHEETY_END"))