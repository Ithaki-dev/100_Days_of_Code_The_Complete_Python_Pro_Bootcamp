
import os
import json
import flight_search # Import the FlightSearch class from flight_search.py
import datetime


# FlightData class
class FlightData:
    def __init__(self, price,origin_airport, destination_airport, out_date, return_date, stops):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops

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

    # Handle empty data if no flight or Amadeus rate limit exceeded
    # UPDATED to include stops!
    if data is None or not data['data']:
        print("No flight data")
        return FlightData(
            price="N/A",
            origin_airport="N/A",
            destination_airport="N/A",
            out_date="N/A",
            return_date="N/A",
            stops="N/A"
        )
    
    # Data from the first flight in the json
    first_flight = data['data'][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    # A flight with 2 segments will have 1 stop
    nr_stops = len(first_flight["itineraries"][0]["segments"]) - 1
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    # Final destination is found in the last segment of the flight
    destination = first_flight["itineraries"][0]["segments"][nr_stops]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    # Return date is the first segment of the second itinerary
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

    # Initialize FlightData with the first flight for comparison
    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, nr_stops)

    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][nr_stops]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            # Add number of stops
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, nr_stops)
            print(f"Lowest price to {destination} is £{lowest_price}")

    return cheapest_flight