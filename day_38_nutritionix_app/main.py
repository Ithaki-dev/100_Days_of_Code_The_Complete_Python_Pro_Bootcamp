# This is an app that allows users to save their daily routine and track their nutrition.
# It uses the Nutritionix API to get nutrition information and the Sheety API to save the data.
import requests
from datetime import datetime
import os

APP_ID = "637f469c"
API_KEY = "16dfc465b9e45ab7bf17d96915618a55"
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/48bf65172daafcb3ac2a7f35015c2f7a/myWorkouts/workouts"

SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
SHEETY_PASSWORD = os.environ.get("SHEETY_PASSWORD")
SHEETY_AUTH = (SHEETY_USERNAME, SHEETY_PASSWORD)

# Get user input for exercise and duration
exercise = input("Tell me which exercise you did: ")
# duration = input("How long did you do it for (in minutes)?: ")

# Get the current date and time
now = datetime.now()
current_date = now.strftime("%d/%m/%Y")
current_time = now.strftime("%H:%M:%S")


# Prepare the headers and parameters for the Nutritionix API request
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
params = {
    "query": exercise,
    # "duration": duration,
    "time": current_time,
    "date": current_date,
    "timezone": "US/Eastern"
}

# Make a request to the Nutritionix API
response = requests.post(NUTRITIONIX_ENDPOINT, headers=headers, json=params)
response.raise_for_status()  # Raise an error for bad responses
exercise_data = response.json()


