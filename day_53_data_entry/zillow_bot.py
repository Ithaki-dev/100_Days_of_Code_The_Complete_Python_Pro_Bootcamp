from pprint import pprint
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfntL5JT4hTnPyHU1QzKG8ruawNa-EZ2_10t0Mih43CbPOHAg/viewform?usp=dialog"
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

def scrap_to_google_form(address, price, link):
    # Create a new instance of the Firefox driver
    driver = webdriver.Firefox()
    # Navigate to the LinkedIn jobs page
    driver.get(GOOGLE_FORM_URL)
    # Wait for the page to load
    sleep(2)

    # Fill out the form fields
    address_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
    address_field.send_keys(address)

    price_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field.send_keys(price)

    link_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
    link_field.send_keys(link)

    # Submit the form
    submit_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    # Note: The XPath for the submit button may vary; adjust it if necessary.
    submit_button.click()

    # Close the browser
    driver.quit()

def submit_rentals_to_google_form():
    """
    Submits the rental listings to the Google Form.
    """
    price_list, address_list, link_list = find_rentals()
    for i in range(len(price_list)):
        scrap_to_google_form(address_list[i], price_list[i], link_list[i])
        sleep(2)  # Wait for 2 seconds before submitting the next form

if __name__ == "__main__":
    submit_rentals_to_google_form()