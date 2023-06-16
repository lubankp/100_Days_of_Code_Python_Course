import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "nnnss67f7e33s231sqw"
USERNAME = "lubpaw91"
GRAPH = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "NotMinor": "yes"
}
# Create a user account
# response = requests.post(url=pixela_endpoint_create, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_configuration = {
    "id": GRAPH,
    "name": "Learning Python",
    "unit": "day",
    "type": "int",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# create a graph
# response = requests.post(url=graph_endpoint, json=graph_configuration, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{GRAPH}"

today = datetime.now()
today_f = today.date().strftime("%Y%m%d")
print(today_f)
pixel_data = {
    "date": today_f,
    "quantity": "1"
}
# create a pixel
# response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{graph_endpoint}/{GRAPH}/{today_f}"
update_pixel_data = {
    "quantity": "1"
}
# Update pixel
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_data, headers=headers)
# print(response.text)

delete_pixel_endpoint = update_pixel_endpoint

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)