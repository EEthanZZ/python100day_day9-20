import requests
from datetime import date
APP_ID = "71e288c1"
API_KEY = "8a74b9a04e9ce45661ba6b0273657538"
END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_END = "https://api.sheety.co/a581b08495e47520093ca6826d9aa89c/myWorkoutsCopy/workouts"


para = {"query": f"{input('what have you done?')}",
        }
headers = {"x-app-id": APP_ID,
           "x-app-key": API_KEY}
today = date.today().strftime("%Y/%m/%d")
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
        "time": today,
        "exercise": exercise,
        "calories": calo

    }
}
sheet_response = requests.post(SHEETY_END, json=sheeety_para)
print(sheet_response.text)