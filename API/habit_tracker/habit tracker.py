import requests
from datetime import datetime
USERNAME = "ethanz"
TOKEN = "aaaabbbbcccc"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_para = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=PIXELA_ENDPOINT, json=PIXELA_para)
# print(response.text)
PIXELA_GRAPH = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_para = {
    "id": "graph1",
    "name": "Daily Water",
    "unit": "cups",
    "type": "int",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
today = datetime(year=2022, month=12, day=2).strftime("%Y%m%d")

response = requests.post(url=PIXELA_GRAPH, json=graph_para, headers=headers)
print(response.text)

PIXELA_GRAPH_POST = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_para['id']}"
graph_post_para = {
    "date": today,
    "quantity": "10"
}
response_2 = requests.post(url=PIXELA_GRAPH_POST, json=graph_post_para, headers=headers)
print(response_2.text)