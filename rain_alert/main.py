import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv("C:/Users/huang/PycharmProjects/EnvironmentVariables/.env")

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv('TWILIO_AUTH')

client = Client(account_sid, auth_token)

OMW_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
OMW_Endpoint_WEATHER = "https://api.openweathermap.org/data/2.5/weather"

ANGELA_KEY = "69f04e4613056b159c2761a9d9e664d2"
API_KEY = "d84c9b97b17ed91817f353713055d75a"

weather_params = {
    "lat": 45.523064,
    "lon": -122.676483,
    "appid": ANGELA_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(OMW_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data["hourly"][:12]

will_rain = False

for hour_data in hourly_data:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_='+18665167229',
        to='+14154256678'
    )

    print(message.status)