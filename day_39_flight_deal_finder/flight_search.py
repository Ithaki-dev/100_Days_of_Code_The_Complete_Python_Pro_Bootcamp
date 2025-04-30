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


# Define FightSearch class

class FlightSearch:
    def __init__(self):
        self.endpoint = FLIGHT_SEARCH_ENDPOINT
        self.api_key = FLIGHT_SEARCH_API_KEY
        self.auth = FLIGHT_SEARCH_AUTH
        self.headers = {
            
            "Content-Type": "application/x-www-form-urlencoded",
        }
        self.params = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.auth,
        }

    def get_access_token(self):
        response = requests.post(f"{self.endpoint}/v1/security/oauth2/token", headers=self.headers, data=self.params)
        if response.status_code == 200:
            access_token = response.json()
            access_token = access_token["access_token"]  # Extract the access token from the response
            return access_token
        else:
            print(f"Error: {response.status_code}")
            return None

    def search_flights(self, origin, destination, date_from, date_to):
        access_token = self.get_access_token()
        print(access_token)
        if access_token:
            headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json",
            }
            params = {
                "fly_from": origin,
                "fly_to": destination,
                "date_from": date_from,
                "date_to": date_to,
                "curr": currency_code,
            }
            response = requests.get(f"{self.endpoint}/v2/search", headers=headers, params=params)
            if response.status_code == 200:
                flight_data = response.json()
                return flight_data
            else:
                print(f"Error: {response.status_code}")
                return None
        else:
            print("Failed to get access token.")
            return None
    
    def add_iata_codes(self, data):
        for city in data:
            if city['iataCode'] == "":
                city['iataCode'] = "TESTING"
        return data

# if __name__ == "__main__":

#     flight_search = FlightSearch()

#     access_token = flight_search.get_access_token()
#     flight_data = flight_search.search_flights("SJO", "LAX", "2023-12-01", "2023-12-15")
#     print(flight_data)