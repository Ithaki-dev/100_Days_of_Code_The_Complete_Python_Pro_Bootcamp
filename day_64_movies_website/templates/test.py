import requests

api_key = "f3a018a56ea8f464a88dc79367cc5433"  # Replace with your TMDB API key
movie_id = 920  # Example: Fight Club

url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'

response = requests.get(url)
if response.status_code == 200:
    movie_data = response.json()
    print(movie_data)
else:
    print("Movie not found or error:", response.status_code)