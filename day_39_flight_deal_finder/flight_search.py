# This class is for seacrhing flights
# It uses the Flight Search API to find flight deals

import os
import json
from dotenv import load_dotenv
import requests
from pprint import pprint

load_dotenv()

# Global variables for the Flight Search API
country_code = "CR"  # Costa Rica
# IATA code for Costa Rica
city_code = "SJO"  # Juan Santamaria International Airport
# currency code for Costa Rica
currency_code = "USD"  # US Dollar

# Get the environment variables
FLIGHT_SEARCH_ENDPOINT = os.getenv('FLIGHT_SEARCH_ENDPOINT')
FLIGHT_SEARCH_API_KEY = os.getenv('FLIGHT_SEARCH_API_KEY')
FLIGHT_SEARCH_AUTH = os.getenv('FLIGHT_SEARCH_AUTH')

# Define header and parameters for the Flight Search API request
headers = {

    "Content-Type": "application/x-www-form-urlencoded",
}
params = {
    "grant_type": "client_credentials",
    "client_id": FLIGHT_SEARCH_API_KEY,
    "client_secret": FLIGHT_SEARCH_AUTH,
}

access_token = requests.post(f"https://test.api.amadeus.com/v1/security/oauth2/token", headers=headers, data=params)
access_token.raise_for_status()  # Raise an error for bad responses
access_token = access_token.json()
access_token = access_token["access_token"]  # Extract the access token from the response
print(f"Access Token: {access_token}")  # Print the access token for debugging
