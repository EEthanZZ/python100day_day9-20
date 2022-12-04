import requests
APP_ID = "71e288c1"
API_KEY = "8a74b9a04e9ce45661ba6b0273657538"
END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

para = {"query": f"{input('what have you done?')}",
        }
headers = {"x-app-id": APP_ID,
           "x-app-key": API_KEY}

nut_post = requests.post(url=END_POINT, json=para, headers=headers)
result = nut_post.json()
print(result)
