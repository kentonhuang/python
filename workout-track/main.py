import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv("C:/Users/huang/PycharmProjects/EnvironmentVariables/.env")

account_sid = os.getenv("NUT_APP_ID")
auth_token = os.getenv('NUT_API_KEY')
bearer = os.getenv("SHEETY_BEARER")

natural_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": account_sid,
    "x-app-key": auth_token
}

print(account_sid)
print(auth_token)

input = input("Tell me what exercise you did: ")

params = {
    "query": input,
    "gender": "male",
    "weight_kg": 81,
    "height_cm": 177.8,
    "age": 29
}

response = requests.post(natural_exercise_endpoint, headers=headers, json=params)
print(response.raise_for_status())
exercises = response.json()['exercises']

sheety_endpoint = "https://api.sheety.co/9651cb4aa43f395444059b0cc87d893d/workoutTracking/workouts"

today = datetime.now()

time = today.strftime("%H:%M:%S")
date = today.strftime("%m/%d/%Y")

for exercise in exercises:
    print(f"{exercise['name']} {exercise['duration_min']} {exercise['nf_calories']}")

    json_body = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }

    sheety_header = {
        "Authorization": f"Bearer {bearer}"
    }

    sheety_response = requests.post(sheety_endpoint, headers=sheety_header, json=json_body)
    print(sheety_response.raise_for_status())
