import requests
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

response = requests.post(url=PIXELA_GRAPH, json=graph_para, headers=headers)
print(response.text)