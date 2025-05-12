# This is a simple price tracker that uses the requests library to scrape prices from a website and send an email if the price drops below a certain threshold.
import requests
import smtplib
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://www.udemy.com/course/the-complete-web-development-bootcamp/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

price = soup.find("span", class_="ud-sr-only")
