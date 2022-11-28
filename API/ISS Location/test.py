import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
if response.status_code == 200:
    print("ok!")

data = response.json()
print(data)
position = data["iss_position"]
print(position)
