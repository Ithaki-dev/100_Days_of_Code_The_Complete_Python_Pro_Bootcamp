import json
import requests

OWM_Endpoint = "http://api.openweathermap.org/data/2.5/forecast"
api_key = ""

weather_params = {
    "lat": 39.48,
    "lon": -0.7532,
    "appid": api_key,
    "units": "metric",
    "cnt": 4  # Number of days to get forecast for

}   

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

# # Check every id of the weather in response and if any of them is less than 700 print umbrella 

weather_data = response.json()["list"]
for weather_element in weather_data:
    if weather_element["weather"][0]["id"] < 700:
        print("It's going to rain today!")
        break