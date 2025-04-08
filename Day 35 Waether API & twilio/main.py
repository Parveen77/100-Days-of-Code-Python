import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env into the environment

api_key = os.getenv("API_KEY")

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"


account_sid = os.getenv("ACCOUNT_SID")

auth_token = os.getenv("AUTH_TOKEN")

weather_params = {
    "lat":22.339430,
    "lon":87.325340,
    "appid":api_key,
    "cnt": 4
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

#data = weather_data["list"][0]["weather"][0]["id"]
#print(data)

expected_rain = False

for hour_weather in weather_data["list"]:
    weather_code = hour_weather["weather"][0]["id"]
    if weather_code < 900:
        expected_rain = True
    
if expected_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_=os.getenv("TWILIO_MOBILE_NUMBER"),
        to=os.getenv("VERIFIED_REAL_NUMBER")
    )
    print(message.status)
