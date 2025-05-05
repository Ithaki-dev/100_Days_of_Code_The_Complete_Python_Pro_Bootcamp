
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
    """
    Finds the cheapest flight from the provided flight data.
    Args:
        data (dict): A dictionary containing flight information. The dictionary is expected
                     to have a key 'data' which is a list of flight details. Each flight detail
                     should include pricing information under 'price' and itinerary details
                     under 'itineraries'.
    Returns:
        FlightData: An instance of the FlightData class containing the details of the cheapest flight.
                    If no data is provided or no flights are available, a FlightData instance with
                    "N/A" values is returned.
    Notes:
        - The function assumes that the flight data is structured in a specific format, where:
          - 'price' contains a key 'grandTotal' representing the total price of the flight.
          - 'itineraries' is a list of flight segments, where each segment contains departure and
            arrival information, including IATA codes and departure times.
        - The function extracts the departure and return dates from the first segment of the
          respective itineraries.
    """
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
    # Return the cheapest flight data
    return cheapest_flight