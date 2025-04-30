# This is for the Data Manager class
# This class is responsible for managing the data in the Google Sheet

#  API variables
import os
import requests
import json
from pprint import pprint

#set environment variables
os.environ['SHEETY_ENDPOINT'] = 'https://api.sheety.co/48bf65172daafcb3ac2a7f35015c2f7a/flightDeals/prices'
os.environ['SHEETY_USERNAME'] = 'rquesada'
os.environ['SHEETY_PASSWORD'] = 'oaksnchwejsbns'
os.environ['SHEETY_SHEET_NAME'] = 'prices'
os.environ['SHEETY_BASIC_AUTH'] = 'Basic cnF1ZXNhZGE6b2Frc25jaHdlanNibnM='

# Get the environment variables
SHEETY_ENDPOINT = os.getenv('SHEETY_ENDPOINT')
SHEETY_USERNAME = os.getenv('SHEETY_USERNAME')
SHEETY_PASSWORD = os.getenv('SHEETY_PASSWORD')
SHEETY_AUTH = (SHEETY_USERNAME, SHEETY_PASSWORD)
SHEETY_BASIC_AUTH = os.getenv('SHEETY_BASIC_AUTH')

# Define the DataManager class
class DataManager:
    def __init__(self):
        self.endpoint = SHEETY_ENDPOINT
        self.auth = SHEETY_AUTH
        self.data = {}
        self.headers = {
            "Authorization": f"{SHEETY_BASIC_AUTH}",
            "Content-Type": "application/json"
        }

    def get_data(self):
        response = requests.get(f"{self.endpoint}", auth=self.auth, headers=self.headers)
        pprint(response.json())
        if response.status_code == 200:
            self.data = response.json()
            return self.data
        else:
            print(f"Error: {response.status_code}")
            return None
        
if __name__ == "__main__":
    data_manager = DataManager()
    data = data_manager.get_data()
    if data:
        print("Data retrieved successfully.")
        if data is not None:
            pprint(data)
        else:
            print("No data to display.")
    else:
        print("Failed to retrieve data.")