# This is an app that allows users to save their daily routine and track their nutrition.
# It uses the Nutritionix API to get nutrition information and the Sheety API to save the data.
import requests
from datetime import datetime
import os

APP_ID = "your_app_id"  # Replace with your actual Nutritionix App ID
API_KEY = "your_api_key"  # Replace with your actual Nutritionix API Key
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/your_sheety_endpoint"  # Replace with your actual Sheety endpoint
SHEETY_USERNAME = "your_sheety_username"  # Replace with your actual Sheety username
SHEETY_PASSWORD = "oyur_sheety_password"  # Replace with your actual Sheety password
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
}

# Make a request to the Nutritionix API
try:
    response = requests.post(NUTRITIONIX_ENDPOINT, headers=headers, json=params)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error fetching data from Nutritionix API: {e}")
    exit(1)\
    
# Make a request to the Sheety API to save the data
try:
    for exercise in data["exercises"]:
        headers = {"Authorization": "Basic cnF1ZXNhZGE6c2R2YWVyeWZjZHZiZHM="}
        sheet_data = {
            "workout": {
                "date": current_date,
                "time": current_time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"],
            }
        }

        # Make a request to the Sheety API
        response = requests.post(SHEETY_ENDPOINT, auth=SHEETY_AUTH, json=sheet_data, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        print("Data saved to Sheety successfully.")
except requests.exceptions.RequestException as e:
    print(f"Error saving data to Sheety API: {e}")
    exit(1)
    


