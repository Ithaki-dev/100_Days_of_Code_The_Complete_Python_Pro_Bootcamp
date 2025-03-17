import requests
from datetime import datetime
LAT = 10.3333
LONG = -84.4333

# response = requests.get(url="http://api.open-notify.org/iss-now.json")

# response.raise_for_status()
# data = response.json()

# latitude = data["iss_position"]["latitude"]

# longitude = data["iss_position"]["longitude"]

# print(f"The International Space Station is currently at {latitude}, {longitude}.")
parameters = {
    "lat": LAT,
    "lng": LONG,
    "formatted": 0,
    "date": datetime.now().strftime("%Y-%m-%d")  # Uncomment to get sunrise and sunset for a specific date

}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)

response.raise_for_status()

data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]

sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()

print(f"Today's sunrise is at {sunrise}.")

print(f"Today's sunset is at {sunset}.")

print(time_now.hour)


