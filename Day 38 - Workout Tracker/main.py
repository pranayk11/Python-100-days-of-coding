import requests
from datetime import datetime
import os

API_KEY = os.environ.get("NT_API_KEY")
APP_ID = os.environ.get("NT_APP_ID")
GENDER = "Male"
WEIGHT = 70
HEIGHT = 171
AGE = 24

BEARER_TOKEN = os.environ.get("SHEET_TOKEN")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ.get("SHEET_ENDPOINT")

exercise_txt = input("Tell me what exercise you did: ")

parameters = {
    "query": "Ran 2 Km",
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(nutritionix_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    headers = {
        "Authorization": f"Bearer {os.environ.get('SHEET_TOKEN')}"
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs, headers=headers)
    print(sheet_response.text)
