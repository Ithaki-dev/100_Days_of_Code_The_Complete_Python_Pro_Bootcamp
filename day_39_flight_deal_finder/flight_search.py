# This class is for seacrhing flights
# It uses the Flight Search API to find flight deals

import os
import json
import requests
from pprint import pprint
# Global variables for the Flight Search API
country_code = "CR"  # Costa Rica
# IATA code for Costa Rica
city_code = "SJO"  # Juan Santamaria International Airport
# currency code for Costa Rica
currency_code = "USD"  # US Dollar

# set environment variables
os.environ['FLIGHT_SEARCH_ENDPOINT'] = 'https://test.api.amadeus.com'
os.environ['FLIGHT_SEARCH_API_KEY'] = 'bAA7mgPqX2APeO736903ZYBDKZGYLeiX'  # Replace with your actual Flight Search API Key
os.environ['FLIGHT_SEARCH_AUTH'] = 'jvjGP6lMd6v5A4EZ'  # Replace with your actual Flight Search API Key
# os.environ['FLIGHT_SEARCH_HEADERS'] = 'your_headers'  # Replace with your actual Flight Search API Key
# os.environ['FLIGHT_SEARCH_PARAMS'] = 'your_params'  # Replace with your actual Flight Search API Key

# Get the environment variables
FLIGHT_SEARCH_ENDPOINT = os.getenv('FLIGHT_SEARCH_ENDPOINT')
FLIGHT_SEARCH_API_KEY = os.getenv('FLIGHT_SEARCH_API_KEY')
FLIGHT_SEARCH_AUTH = os.getenv('FLIGHT_SEARCH_AUTH')
# FLIGHT_SEARCH_HEADERS = os.getenv('FLIGHT_SEARCH_HEADERS')
# FLIGHT_SEARCH_PARAMS = os.getenv('FLIGHT_SEARCH_PARAMS')

# Define header and parameters for the Flight Search API request
headers = {
    
    "Content-Type": "application/flight_search",
}
params = {
    "grant_type": "client_credentials",
    "client_id": FLIGHT_SEARCH_API_KEY,
    "client_secret": FLIGHT_SEARCH_AUTH,
}

access_token = requests.post(f"{FLIGHT_SEARCH_ENDPOINT}/v1/security/oauth2/token",headers=headers, params=params)
access_token.raise_for_status()  # Raise an error for bad responses
access_token = access_token.json()
access_token = access_token["access_token"]  # Extract the access token from the response
print(f"Access Token: {access_token}")  # Print the access token for debugging
