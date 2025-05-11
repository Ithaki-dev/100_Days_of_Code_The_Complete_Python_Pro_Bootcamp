"""
This script creates a Spotify playlist from a list of songs scraped from the Billboard Hot 100 website for a specified date.
Modules:
    - os: Provides functions for interacting with the operating system.
    - pprint: Used for pretty-printing data structures.
    - requests: Allows sending HTTP requests to fetch data from the web.
    - bs4 (BeautifulSoup): Used for parsing HTML and extracting data from web pages.
    - spotipy: A lightweight Python library for the Spotify Web API.
    - dotenv: Loads environment variables from a .env file.
Environment Variables:
    - SPOTIFY_CLIENT_ID: Spotify API client ID.
    - SPOTIFY_CLIENT_SECRET: Spotify API client secret.
    - SPOTIFY_REDIRECT_URI: Spotify API redirect URI.
Workflow:
    1. Prompts the user to input a date in the format YYYY-MM-DD.
    2. Scrapes the Billboard Hot 100 chart for the specified date to extract song titles and artist names.
    3. Authenticates with the Spotify API using the Spotipy library.
    4. Searches for the scraped songs on Spotify and retrieves their URIs.
    5. Creates a private Spotify playlist named "Billboard 100 year <YEAR>".
    6. Adds the found songs to the created playlist.
    7. Outputs the playlist URL.
Functions:
    - None (all logic is implemented in the main script).
Usage:
    Run the script and follow the prompts to create a Spotify playlist for a specific date.
Dependencies:
    - Install the required libraries using `pip install requests beautifulsoup4 spotipy python-dotenv`.
Notes:
    - Ensure that the .env file contains valid Spotify API credentials.
    - The script handles cases where songs are not found on Spotify by skipping them and printing a message.
"""

import os
from pprint import pprint
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
SPOTIFY_REDIRECT_URI = os.environ.get("SPOTIFY_REDIRECT_URI")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
# Ask the user for the year they want to travel to
year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{year}/"

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
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="playlist-modify-private",
    cache_path=os.path.join(current_path, ".cache-spotify"),
))
# Check if the user is authenticated
if not sp:
    print("Error: Unable to authenticate with Spotify API")
    exit()
else:
    print("Successfully authenticated with Spotify API")
    print("User ID:", sp.me()["id"])
# Search for songs on Spotify
song_uris = []
for song, artist in zip(list_of_songs, list_of_artists):
    query = f"{song} {artist}"
    result = sp.search(q=query, type="track", limit=1)
    if result["tracks"]["items"]:
        song_uris.append(result["tracks"]["items"][0]["uri"])
    else:
        print(f"Song not found on Spotify: {song} by {artist}")
#pprint(song_uris)
# Create a new playlist
playlist_name = "Billboard 100 year " + year.split("-")[0]
playlist_description = "Top 100 songs from Billboard"
user_id = sp.me()["id"]
playlist = sp.user_playlist_create(
    user=user_id,
    name=playlist_name,
    public=False,
    description=playlist_description
)
# Add songs to the playlist
if song_uris:
    sp.user_playlist_add_tracks(
        user=user_id,
        playlist_id=playlist["id"],
        tracks=song_uris
    )
    print(f"Successfully added {len(song_uris)} songs to the playlist '{playlist_name}'")
else:
    print("No songs found to add to the playlist")
# Print the playlist URL
playlist_url = playlist["external_urls"]["spotify"]
print(f"Playlist URL: {playlist_url}")