# This app create a spotify playlist from a list of songs scrapped from a website
# It uses the Spotify API to create a playlist and add songs to it

import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Current path
current_path = os.path.dirname(os.path.abspath(__file__))

# Set up Spotify API credentials
SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
print(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)

#year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = "https://www.billboard.com/charts/hot-100/2014-05-17/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, headers=headers)
response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
if response.status_code != 200:
    print(f"Error: {response.status_code}")
    exit()

webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
# print(soup.prettify())

songs = soup.find_all("li", class_="lrv-u-width-100p")
list_of_songs = []
list_of_artists = []
for tag in songs:
    artist_name = tag.find("span", class_="c-label")
    if not artist_name or len(artist_name.text.strip()) < 3:
        continue
    list_of_artists.append(artist_name.getText().strip())

for tag in songs:
    song_name = tag.find("h3")
    if not song_name:
        continue
    list_of_songs.append(song_name.getText().strip())

# Connect to Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri="https://example.com/callback",
    scope="playlist-modify-private" 
))
# Check if the user is authenticated
if not sp:
    print("Error: Unable to authenticate with Spotify API")
    exit()
else:
    print("Successfully authenticated with Spotify API")
    print("User ID:", sp.me()["id"])