import requests
import datetime
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env into the environment


NUTRITIONX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

API_KEY= os.getenv("API_KEY")
APP_ID = os.getenv("APP_ID")

AUTH_TOKEN_SHEETY = os.getenv("AUTH_TOKEN_SHEETY")
USERNAME_SHEETY = os.getenv("USERNAME_SHEETY")
PASSWORD_SHEETY = os.getenv("PASSWORD_SHEETY")

nutri_headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
  }

exercise_text = input("Tell me which exercises you did: ")


nutri_params = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg" : 70,
    "height_cm" : 171,
    "age" : 25,
}

response = requests.post(NUTRITIONX_ENDPOINT, json=nutri_params, headers=nutri_headers)
response.raise_for_status()
result = response.json()


sheety_endpoints = "https://api.sheety.co/ee58af7e3286940458d54e3198bc1d71/myWorkouts/workouts"

DATE = datetime.now().strftime("%d/%m/%Y")
TIME = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    exercise_params = {
        "workout" : {
            "date" : DATE,
            "time" : TIME,
            "exercise" : exercise["name"].title(),
            "duration" : exercise["duration_min"],
            "calories" : exercise["nf_calories"],
        }
    }

#sheety_response = requests.post(sheety_endpoints, json=exercise_params)

#sheety_response = requests.post(
#  sheety_endpoints, 
#  json=exercise_params, 
#  auth=(
#      USERNAME_SHEETY, 
#      PASSWORD_SHEETY,
#  )
#)

#Bearer Token Authentication
bearer_headers = {
"Authorization": f"Bearer {AUTH_TOKEN_SHEETY}"
}
sheety_response = requests.post(
    sheety_endpoints, 
    json=exercise_params, 
    headers=bearer_headers
)

sheety_response.raise_for_status()

print(sheety_response.text)



