# This class is for seacrhing flights
# It uses the Flight Search API to find flight deals

import os
import requests
from pprint import pprint

# set environment variables
os.environ['FLIGHT_SEARCH_ENDPOINT'] = 'https://tequila-api.kiwi.com/v2/search'
os.environ['FLIGHT_SEARCH_API_KEY'] = 'your_api_key'  # Replace with your actual Flight Search API Key
os.environ['FLIGHT_SEARCH_AUTH'] = 'your_auth_key'  # Replace with your actual Flight Search API Key
os.environ['FLIGHT_SEARCH_HEADERS'] = 'your_headers'  # Replace with your actual Flight Search API Key
os.environ['FLIGHT_SEARCH_PARAMS'] = 'your_params'  # Replace with your actual Flight Search API Key

# Get the environment variables
FLIGHT_SEARCH_ENDPOINT = os.getenv('FLIGHT_SEARCH_ENDPOINT')
FLIGHT_SEARCH_API_KEY = os.getenv('FLIGHT_SEARCH_API_KEY')
FLIGHT_SEARCH_AUTH = os.getenv('FLIGHT_SEARCH_AUTH')
FLIGHT_SEARCH_HEADERS = os.getenv('FLIGHT_SEARCH_HEADERS')
FLIGHT_SEARCH_PARAMS = os.getenv('FLIGHT_SEARCH_PARAMS')

# Define the FlightSearch class