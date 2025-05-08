# This scrip is for scraping a website using BeautifulSoup

from bs4 import BeautifulSoup
import os
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_website = response.text
soup = BeautifulSoup(yc_website, "html.parser")


article_tag = soup.find(name="span", class_="titleline")
if article_tag:
	article_text = article_tag.getText()
	article_link = article_tag.find("a").get("href")
	article_score = soup.find(name="span", class_="score")
	article_score_number = article_score.getText().split()[0] if article_score else "No score available"
	
	print(article_text)
	print(article_link)
	print(article_score_number)
else:
	print("No article found with the specified class.")


# Explaining the code
# current_directory = os.path.dirname(os.path.abspath(__file__))
# html_file_path = os.path.join(current_directory, "website.html")

# with open(html_file_path, "r", encoding="utf-8") as file:
#     contents = file.read()
#     soup = BeautifulSoup(contents, "html.parser")
#     #print(soup.prettify())
#     # print(soup.title.string)
#     # print(soup.title)
#     # print(soup.title.name)
#     # print(soup.head)
#     # print(soup.head.title)
#     headings = soup.find_all("a")
#     for heading in headings:
#         print(heading.get("href"))