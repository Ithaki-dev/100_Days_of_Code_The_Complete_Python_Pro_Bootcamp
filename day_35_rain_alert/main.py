import json
import requests
import os
from twilio.rest import Client

# Weather API
OWM_Endpoint = "http://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get('OWM_API_KEY')
# Twilio API
account_sid = 'AC1d9ace12d1f4b751050e6e1ff6fa0059'
auth_token = os.environ.get('AUTH_TOKEN_TWILIO')
print(auth_token,api_key)



# Coordinates of the location where you want to check the weather
weather_params = {
    "lat": 38.71,
    "lon": -9.13,
    "appid": api_key,
    "units": "metric",
    "cnt": 4  # Number of days to get forecast for

}   

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

# # Check every id of the weather in response and if any of them is less than 700 print umbrella 

def send_SMS():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
            from_='+13312461663',
            body='Its going to rain',
            to='+50660437458'
        )
    print(message.sid)

weather_data = response.json()["list"]
for weather_element in weather_data:
    if weather_element["weather"][0]["id"] < 700:
        print("It's going to rain today!")
        send_SMS()
        break