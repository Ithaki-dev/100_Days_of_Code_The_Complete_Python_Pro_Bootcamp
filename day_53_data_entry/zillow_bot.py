from pprint import pprint
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfntL5JT4hTnPyHU1QzKG8ruawNa-EZ2_10t0Mih43CbPOHAg/viewform?usp=header"

def find_rentals():
    """
    Fetches rental listings from Zillow and returns a list of dictionaries
    containing the address, price, and link for each listing.
    """
    url = "https://appbrewery.github.io/Zillow-Clone/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }
    response = requests.get(url, headers=headers)
    webpage = response.text
    soup = BeautifulSoup(webpage, "html.parser")

    # Find the rental listings in the HTML
    rental_listings = soup.find_all("li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

    # Extract the relevant information from each listing
    
    price_list = []
    address_list = []
    link_list = []
    for listing in rental_listings:
        address = listing.find("address").text
        price = listing.find("span", class_="PropertyCardWrapper__StyledPriceLine").text
        link = listing.find("a", class_="StyledPropertyCardDataArea-anchor")["href"]
        # format address erase from san francisco and postcode
        address = address.replace("\n", "").strip()
        address = address.replace(", CA", "")
        address = address.replace("San Francisco", "").strip()
        # pprint(address)

        # Format price
        price = price.replace("\n", "").strip()
        price = price.replace(" ", "").replace("+/mo", "").replace("/mo", "").replace("+1bd", "")
        price = f"{price}"
        # pprint(price)

        link = link.replace("\n", "").strip()

        price_list.append(price)
        address_list.append(address)
        link_list.append(link)
  
    return price_list, address_list, link_list


if __name__ == "__main__":
    rentals = find_rentals()
    pprint(rentals)