from datetime import datetime, timedelta
import os
import json
from dotenv import load_dotenv
import requests

load_dotenv()

# Get the environment variables
FLIGHT_SEARCH_ENDPOINT = os.getenv('FLIGHT_SEARCH_ENDPOINT')
FLIGHT_SEARCH_API_KEY = os.getenv('FLIGHT_SEARCH_API_KEY')
FLIGHT_SEARCH_AUTH = os.getenv('FLIGHT_SEARCH_AUTH')


# Define FlightSearch class

class FlightSearch:
    """
    FlightSearch is a class that interacts with a flight search API to retrieve flight information,
    city IATA codes, and perform flight searches based on user-provided criteria.
    Attributes:
        endpoint (str): The base URL for the flight search API.
        api_key (str): The API key for authenticating requests.
        auth (str): The client secret for authenticating requests.
        headers (dict): Default headers for API requests.
        params (dict): Default parameters for obtaining an access token.
    Methods:
        get_access_token():
            Retrieves an access token from the flight search API for authentication.
            Returns:
                str: The access token if successful, None otherwise.
        get_city_code(city_name):
            Retrieves the IATA code for a given city.
            Args:
                city_name (str): The name of the city to search for.
            Returns:
                str: The IATA code of the city if found, None otherwise.
        add_iata_codes(data):
            Updates a list of city dictionaries with their corresponding IATA codes.
            Args:
                data (list): A list of dictionaries, each containing a 'city' key and an 'iataCode' key.
            Returns:
                list: The updated list of dictionaries with IATA codes added.
        flight_search(destination, departure_date, return_date):
            Searches for flights based on the provided destination, departure date, and return date.
            Args:
                destination (str): The IATA code of the destination city.
                departure_date (str): The departure date in the format 'YYYY-MM-DD'.
                return_date (str): The return date in the format 'YYYY-MM-DD'.
            Returns:
                dict: The JSON response from the flight search API containing flight offers.
    """
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
    
    def flight_search(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):
        access_token = self.get_access_token()
        # print(f"Access token: {access_token}")  # Debugging: Print the access token
        headers = {
            "Authorization": f"Bearer {access_token}",
        }
        params = {
            "originLocationCode": origin_city_code,  # Use the provided origin city code
            "destinationLocationCode": destination_city_code,  # Ensure this is a valid IATA code
            "departureDate": from_time,  # Ensure the date format is YYYY-MM-DD
            "returnDate": to_time,  # Ensure the date format is YYYY-MM-DD
            "nonStop": "true" if is_direct else "false",  # Set to true for direct flights only
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
    # test flight search metohd
    flight_search = FlightSearch()
    origin_city_code = "SJO"  # Example origin city code
    destination_city_code = "LAX"  # Example destination city code
    from_time = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")  # Tomorrow's date
    to_time = (datetime.now() + timedelta(days=60)).strftime("%Y-%m-%d")  # Two months from now
    is_direct = True  # Set to True for direct flights only
    flight_data = flight_search.flight_search(origin_city_code, destination_city_code, from_time, to_time, is_direct)
    print(flight_data)  # Print the flight data for testing
