# This class is for seacrhing flights
# It uses the Flight Search API to find flight deals

from datetime import datetime, timedelta
import os
import json
from dotenv import load_dotenv
import requests
from pprint import pprint

load_dotenv()

# Get the environment variables
FLIGHT_SEARCH_ENDPOINT = os.getenv('FLIGHT_SEARCH_ENDPOINT')
FLIGHT_SEARCH_API_KEY = os.getenv('FLIGHT_SEARCH_API_KEY')
FLIGHT_SEARCH_AUTH = os.getenv('FLIGHT_SEARCH_AUTH')


# Define FlightSearch class

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

    def get_city_code(self, city_name):
        access_token = self.get_access_token()
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }
        params = {
            "keyword": city_name,  # City to search
            "include": "AIRPORTS"  # Include airports
        }
        # This method is for getting the IATA code for a city
        response = requests.get(f"{self.endpoint}/v1/reference-data/locations/cities", headers=headers, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        # Parse the response
        json_data = response.json()
        if json_data['data']:
            return json_data['data'][0]['iataCode']
        else:
            print(f"No IATA code found for {city_name}.")
            return None

    def add_iata_codes(self, data):
        for city in data:
            if city['iataCode'] == "":
                # Get the IATA code for the city
                city_name = city['city']
                iata_code = self.get_city_code(city_name)
                if iata_code:
                    city['iataCode'] = iata_code
                else:
                    print(f"Could not find IATA code for {city_name}.") 
        return data
    
    def flight_search(self, destination, departure_date, return_date):
        access_token = self.get_access_token()
        headers = {
            "Authorization": f"Bearer {access_token}",
        }
        params = {
            "originLocationCode": "SJO",  # Replace with a valid origin IATA code if needed
            "destinationLocationCode": destination,  # Ensure this is a valid IATA code
            "departureDate": departure_date,  # Ensure the date format is YYYY-MM-DD
            "returnDate": return_date,  # Ensure the date format is YYYY-MM-DD
            "nonStop": "false",  # Allow both non-stop and connecting flights for more results
            "adults": 1,
            "currencyCode": "USD",  # Ensure currency code is included
            "max": 10  # Increase the number of results for testing
        }
        response = requests.get(
            f"{self.endpoint}/v2/shopping/flight-offers",
            headers=headers,
            params=params
        )
        response.raise_for_status()  # Raise an error for bad responses
        
        if response.status_code != 200:
            print(f"Error: {response.status_code}, {response.text}")  # Log detailed error
        # Parse the response
        json_data = response.json()
        # save the response to a JSON file for debugging
        with open("flight_search_response.json", "w") as f:
            json.dump(json_data, f, indent=4)

        return json_data  # Return the JSON data for further processing


if __name__ == "__main__":

    flight_search = FlightSearch()
    # test the flight search
    
    # test the get_city_code method

    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    six_month_from_today = (datetime.now() + timedelta(days=(6 * 30))).strftime("%Y-%m-%d")


    test = flight_search.flight_search("LAX", tomorrow, six_month_from_today)
    print(test)




    