# This is a simple price tracker that uses the requests library to scrape prices from a website and send an email if the price drops below a certain threshold.
import requests
import smtplib
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from pprint import pprint


def find_price():
    """
    Fetches the price of a product from a specified Amazon product page.
    This function sends an HTTP GET request to the provided Amazon product URL
    with custom headers to mimic a browser request. It then parses the HTML
    response using BeautifulSoup to extract the price of the product.
    Returns:
        float: The price of the product as a float if found.
        None: If the price element is not found on the webpage.
    Notes:
        - The function assumes the price is located in the third element of
          the list returned by `soup.find_all` with the class "a-price-whole".
        - The function removes commas from the price string before converting
          it to a float.
        - If the price element is not found, the function prints a message
          and returns None.
    Raises:
        None: This function does not explicitly handle exceptions. Ensure
              proper error handling for network issues or changes in the
              webpage structure.
    """
    url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }
    response = requests.get(url, headers=headers)
    webpage = response.text
    soup = BeautifulSoup(webpage, "html.parser")
    
    # Find the price element in the HTML
    
    price = soup.find_all("span", class_="a-price-whole")
    if not price:
        print("Price not found")
        return None
    # The price is third element in the list
    price = price[2].get_text()
    # Remove commas and convert to float
 
    price = float(price)
    return price

def send_email(price):
    my_email = os.getenv("MY_EMAIL")
    password = os.getenv("PASSWORD")
    to_email = os.getenv("TO_EMAIL")

    subject = "Price Drop Alert!"
    body = f"The price has dropped to ${price}!"
    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=message)

if __name__ == "__main__":
    load_dotenv()
    price = find_price()
    print(f"Current price: ${price}")
    if price and price < 100:  # Set your desired price threshold here
        send_email(price)
    else:
        print(f"Price is above the threshold, the current price is: {price}")