import requests
from datetime import datetime
import os

API_KEY = os.environ["API_KEY"]
API_ID = os.environ["API_ID"]
ENDPOINT = os.environ["ENDPOINT"]

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

exercise = input("Tell me which exercises you did: ")

parameters = {
    "query": f"{exercise}",
    "gender": "male",
    "weight_kg": 74,
    "height_cm": 173,
    "age": 31
}

response = requests.post(ENDPOINT, headers=headers, json=parameters)
result = response.json()
exercises = result["exercises"]
exercise_list = []

SHEETY_ENDPOINT_GET = os.environ["SHEETY_ENDPOINT_GET"]
SHEETY_ENDPOINT_POST = os.environ["SHEETY_ENDPOINT_POST"]

today = datetime.now()
date = today.date().strftime("%Y/%m/%d")
time = today.time().strftime("%H:%M:%S")

USER = os.environ["USER"]
PASSWORD = os.environ["PASSWORD"]


for exercise in exercises:
    arkusz1 = {
        "arkusz1": {
            "date": date,
            "time": time,
            "exercise": exercise["user_input"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    print(arkusz1)
    response2 = requests.post(url=SHEETY_ENDPOINT_POST, json=arkusz1, auth=(USER, PASSWORD))
    result = response2.text
    print(result)
