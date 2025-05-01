# This is for the Data Manager class
# This class is responsible for managing the data in the Google Sheet

#  API variables
import os
import requests
import json
from pprint import pprint
from dotenv import load_dotenv


load_dotenv()

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
        response = requests.get(f"{self.endpoint}", headers=self.headers)
        if response.status_code == 200:
            self.data = response.json()
            # get the data from prices
            sheet_data = self.data['prices']
            return sheet_data
        else:
            print(f"Error: {response.status_code}")
            return None
        
    def update_data(self, data):
        for item in data:
            response = requests.put(f"{self.endpoint}/{item['id']}", json={"price": item}, headers=self.headers)
            if response.status_code == 200:
                print(f"Data updated successfully for ID: {item['id']}")
            else:
                print(f"Error updating data for ID: {item['id']}. Status code: {response.status_code}")
        
if __name__ == "__main__":
    data_manager = DataManager()

    new_data = DataManager()
    new_data.update_data(data_test)

    updated_data = new_data.get_data()
    print(updated_data)
    