# This is an app for search cheap flights
# It uses the Flight Search API to find flight deals
# It uses the Data Manager to save the data in a Google Sheet
# It uses Twilio to send SMS messages with the flight deals

import os
# from flight_data import FlightData
# from flight_search import FlightSearch
from data_manager import DataManager
# from notification_manager import NotificationManager

prices = DataManager()
sheety_data = prices.get_data()
if sheety_data is not None:
    print("Data retrieved successfully.")
    print(sheety_data)