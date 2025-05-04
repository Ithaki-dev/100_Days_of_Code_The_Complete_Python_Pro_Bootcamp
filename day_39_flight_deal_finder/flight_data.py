# This is the class that handles the flight data and API calls for the Flight Deal Finder project.

import os
import json
import flight_search # Import the FlightSearch class from flight_search.py
import datetime


# FlightData class
class FlightData:
    def __init__(self, price,origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date


def find_cheapest_flight(data):
    # This method is for finding the cheapest flight from the data

    # Check if data is None or empty
    if data is None:
        print("No data found")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")
    # Check if the data list is empty
    if not data.get('data'):
        print("No flights available")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")
    
    # Data from the first flight in the list
    first_flight = data['data'][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
    # Initialize cheapest_flight with the first flight data
    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)

    # Loop through the data to find the cheapest flight
    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)
            print(f"Lowest price to {destination} is £{lowest_price}")
    # Return the cheapest flight data
    return cheapest_flight


    
