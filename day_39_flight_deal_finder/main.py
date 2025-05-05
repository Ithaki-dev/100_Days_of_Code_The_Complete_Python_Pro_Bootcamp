
"""
This script is an application for searching cheap flights using the Flight Search API. 
It integrates with a Google Sheet to manage flight data and uses Twilio to send SMS notifications 
for flight deals.
Modules:
- datetime: For handling date and time operations.
- os: For interacting with the operating system.
- flight_data: Contains functionality to find the cheapest flight.
- flight_search: Handles flight search operations using the Flight Search API.
- data_manager: Manages data storage and retrieval from a Google Sheet.
- notification_manager: Sends notifications via SMS using Twilio.
Classes:
- DataManager: Handles data retrieval and updates for the Google Sheet.
- FlightSearch: Provides methods to search for flights and retrieve IATA codes.
- NotificationManager: Sends SMS notifications for flight deals.
Workflow:
1. Retrieve flight data from a Google Sheet using the DataManager.
2. Update missing IATA codes in the Google Sheet by fetching them from the Flight Search API.
3. Search for flights for each destination over a specified date range (from tomorrow to six months from today).
4. Identify the cheapest flight for each destination.
5. Compare the flight price with the lowest price recorded in the Google Sheet.
6. If a cheaper flight is found, send an SMS notification with the flight details.
Note:
- The script pauses for 2 seconds after updating each IATA code to avoid hitting API rate limits.
- Ensure that the required API keys and credentials for the Flight Search API, Google Sheets API, and Twilio are properly configured.
"""

import datetime
from datetime import timedelta
import os
import time
from flight_data import find_cheapest_flight
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from dateutil.relativedelta import relativedelta

data_manager = DataManager()
sheet_data = data_manager.get_data()
user_emails = data_manager.get_users()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Define the origin city IATA code
ORIGIN_CITY_IATA = "SJO"  # Replace "LON" with the appropriate IATA code for your origin city

# Update the IATA codes in the Google Sheet
for row in sheet_data:
    if row["iataCode"] == "":
        # Get the IATA code for the city
        city_name = row["city"]
        iata_code = flight_search.get_city_code(city_name)
        row["iataCode"] = iata_code
        data_manager.update_data(sheet_data)
        time.sleep(2)


# ==================== Search for direct flights  ====================

tomorrow = (datetime.datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
six_month_from_today = (datetime.datetime.now() + relativedelta(months=6)).strftime("%Y-%m-%d")

for destination in sheet_data:
    print(f"Getting direct flights for {destination['city']}...")
    flights = flight_search.flight_search(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: ${cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)

    # ==================== Search for indirect flight if N/A ====================

    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flight_search.flight_search(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct=False
        )
        cheapest_flight = find_cheapest_flight(stopover_flights)
        print(f"Cheapest indirect flight price is: ${cheapest_flight.price}")

    # ==================== Send notification and emails ====================
    # Check if the flight is N/A (not available)
    if cheapest_flight.price == "N/A":
        print(f"No flights available for {destination['city']}.")
        continue

    if int(cheapest_flight.price) < destination["lowestPrice"]:
        print(f"Price drop! New price: ${cheapest_flight.price}")
        message = f"Low price alert! Only ${cheapest_flight.price} to fly from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, from {cheapest_flight.out_date} to {cheapest_flight.return_date}."
        notification_manager.send_message(message)

        # Send email to all users
        for user in user_emails:
            notification_manager.send_email(message, user["email"])
            print(f"Email sent to {user['email']}")

        
