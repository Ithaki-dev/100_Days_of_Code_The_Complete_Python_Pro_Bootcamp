import json
import requests

OWM_Endpoint = "http://api.openweathermap.org/data/2.5/forecast"
api_key = "ca07893fbf4a5b125b26df9a51a181c1"

weather_params = {
    "lat":10.3238,
    "lon":-84.4271,
    "appid": api_key

}
    

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.json())


# Convert the dictionary to a JSON string
weather_data_json = json.dumps(response.json())
# save response in json format file
with open('weather_data.json', 'w') as f:
    f.write(weather_data_json)
