# This scrip is for scraping a website using BeautifulSoup

from bs4 import BeautifulSoup
import os
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_website = response.text
soup = BeautifulSoup(yc_website, "html.parser")


article = soup.find_all(name="span", class_="titleline")

if article:
	article_text = []
	article_link = []
	article_score_number = []
	for tag in article:
		article_text.append(tag.getText())
		link_tag = tag.find("a")
		article_link.append(link_tag.get("href") if link_tag else "No link available")
		article_score = tag.find_next(name="span", class_="score")
		article_score_number.append(int(article_score.getText().split()[0] if article_score else "0"))
	
	# print(article_text)
	# print(article_link)
	# print(article_score_number)
	# Finding the article with the highest score
	max_score = max(article_score_number)
	max_index = article_score_number.index(max_score)
	print(f"Article with the highest score: {article_text[max_index]}, with {max_score} points.")

    
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