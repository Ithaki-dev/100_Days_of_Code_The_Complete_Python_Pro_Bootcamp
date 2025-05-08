# This scrip is for scraping a website using BeautifulSoup

from bs4 import BeautifulSoup
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
html_file_path = os.path.join(current_directory, "website.html")

with open(html_file_path, "r", encoding="utf-8") as file:
    contents = file.read()
    soup = BeautifulSoup(contents, "html.parser")
    #print(soup.prettify())
    # print(soup.title.string)
    # print(soup.title)
    # print(soup.title.name)
    # print(soup.head)
    # print(soup.head.title)
    headings = soup.find_all("a")
    for heading in headings:
        print(heading.get("href"))