import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_para = {
    "token": "aaaabbbbcccc",
    "username": "ethanz",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
response = requests.post(url=PIXELA_ENDPOINT, json=PIXELA_para)
print(response.text)