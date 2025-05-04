# This is an app for search cheap flights
# It uses the Flight Search API to find flight deals
# It uses the Data Manager to save the data in a Google Sheet
# It uses Twilio to send SMS messages with the flight deals

import datetime
import os
import pprint
from flight_data import find_cheapest_flight
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Update the IATA codes in the Google Sheet
for row in sheet_data:
    if row["iataCode"] == "":
        # Get the IATA code for the city
        city_name = row["city"]
        iata_code = flight_search.get_city_code(city_name)
        row["iataCode"] = iata_code
        data_manager.update_data(sheet_data)
        datetime.time.sleep(2)


#  search for flights
tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
six_month_from_today = datetime.datetime.now() + datetime.timedelta(days=(6 * 30))

for destination in sheet_data:
    # Get the IATA code for the destination
    destination_code = destination["iataCode"]
    # Get the flight data from the API
    flight_data = flight_search.flight_search(destination_code, tomorrow.strftime("%Y-%m-%d"), six_month_from_today.strftime("%Y-%m-%d"))
    # print(flight_data)

    # Find the cheapest flight
    cheapest_flight = find_cheapest_flight(flight_data)
    # Print the cheapest flight data
    # print("the cheapest flight data is:")
    # pprint.pprint(cheapest_flight.__dict__)

    # Check if the flight is cheaper than the price in the Google Sheet
    if cheapest_flight.price < destination["lowestPrice"]:
        # Send a message with the flight details
        message = f"Low price alert! Only £{cheapest_flight.price} to fly from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport} from {cheapest_flight.out_date} to {cheapest_flight.return_date}."
        notification_manager.send_message(message)
        print(message)
    else:
        print("No cheap flights found.")
#     # Uncomment the line below to send a message with the flight details