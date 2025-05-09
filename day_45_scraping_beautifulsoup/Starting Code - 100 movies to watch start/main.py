import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

soup = BeautifulSoup(requests.get(URL).text, "html.parser")
movies = soup.find_all("h3", class_="title")
movie_titles = [movie.get_text() for movie in movies]
print(movie_titles)
with open("movies.txt", "w") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")
