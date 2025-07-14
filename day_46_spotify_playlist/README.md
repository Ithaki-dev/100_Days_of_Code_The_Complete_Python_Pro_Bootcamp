# 🎵 Spotify Billboard Playlist Creator

A Python application that creates personalized Spotify playlists based on Billboard Hot 100 charts from any date. Travel back in time and rediscover the top songs from your favorite year!

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Spotify](https://img.shields.io/badge/Spotify-API-green)
![Billboard](https://img.shields.io/badge/Billboard-Hot%20100-red)
![Web Scraping](https://img.shields.io/badge/Web%20Scraping-BeautifulSoup-orange)

## 🌟 Features

### 🎯 Core Functionality
- **Date-based Chart Scraping**: Extract Billboard Hot 100 songs from any specified date
- **Spotify Integration**: Automatically search and add songs to your Spotify account
- **Playlist Creation**: Generate private playlists with descriptive names
- **Smart Song Matching**: Intelligent search algorithm to find songs on Spotify
- **Error Handling**: Graceful handling of missing songs and API errors

### 🔍 Web Scraping
- **Billboard Hot 100**: Scrapes song titles and artist names from Billboard.com
- **Robust Parsing**: Uses BeautifulSoup for reliable HTML parsing
- **User-Agent Headers**: Mimics browser requests to avoid blocking
- **Data Validation**: Filters out invalid or incomplete song data

### 🎶 Spotify Features
- **OAuth Authentication**: Secure authentication with Spotify Web API
- **Private Playlists**: Creates private playlists that only you can see
- **Batch Song Addition**: Efficiently adds multiple songs to playlists
- **URI Management**: Handles Spotify track URIs for playlist operations

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Spotify Premium account (recommended)
- Spotify Developer account for API access

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/spotify-billboard-playlist.git
   cd spotify-billboard-playlist
   ```

2. **Create and activate virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Spotify API Setup

1. **Create a Spotify App:**
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
   - Click "Create an App"
   - Fill in app name and description
   - Note your `Client ID` and `Client Secret`

2. **Configure Redirect URI:**
   - In your Spotify app settings, add redirect URI: `http://localhost:8080`
   - Or use your preferred redirect URI

3. **Create environment file:**
   ```bash
   # Create .env file in project root
   touch .env
   ```

4. **Add your credentials to .env:**
   ```env
   SPOTIFY_CLIENT_ID=your_client_id_here
   SPOTIFY_CLIENT_SECRET=your_client_secret_here
   SPOTIFY_REDIRECT_URI=http://localhost:8080
   ```

### Running the Application

```bash
python main.py
```

## 📋 Usage Guide

### Step-by-Step Instructions

1. **Run the application:**
   ```bash
   python main.py
   ```

2. **Enter a date:**
   ```
   Which year do you want to travel to? Type the date in this format YYYY-MM-DD: 2020-03-15
   ```

3. **Authenticate with Spotify:**
   - Browser will open automatically
   - Log in to your Spotify account
   - Authorize the application
   - Copy the redirect URL back to the terminal if prompted

4. **Wait for processing:**
   - The app will scrape Billboard Hot 100 for your date
   - Search for each song on Spotify
   - Create a new playlist
   - Add found songs to the playlist

5. **Enjoy your playlist:**
   - Check your Spotify account for the new playlist
   - Playlist will be named "Billboard 100 year YYYY"

### Example Output

```
Successfully authenticated with Spotify API
User ID: your_spotify_username
Song not found on Spotify: Some Obscure Song by Unknown Artist
Successfully added 87 songs to the playlist 'Billboard 100 year 2020'
Playlist URL: https://open.spotify.com/playlist/4uVxy6W8rlGnYVfOaGCWr5
```

## 🛠️ Technical Details

### Dependencies

```python
import os                    # Environment and file operations
import requests              # HTTP requests for Billboard scraping
from bs4 import BeautifulSoup  # HTML parsing
import spotipy               # Spotify Web API client
from spotipy.oauth2 import SpotifyOAuth  # OAuth authentication
from dotenv import load_dotenv  # Environment variable management
from pprint import pprint    # Pretty printing for debugging
```

### Core Components

#### 1. Web Scraping Module
```python
# Billboard Hot 100 scraping
url = f"https://www.billboard.com/charts/hot-100/{year}/"
soup = BeautifulSoup(webpage, "html.parser")
songs = soup.find_all("li", class_="lrv-u-width-100p")
```

#### 2. Spotify Authentication
```python
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="playlist-modify-private"
))
```

#### 3. Song Search Algorithm
```python
for song, artist in zip(list_of_songs, list_of_artists):
    query = f"{song} {artist}"
    result = sp.search(q=query, type="track", limit=1)
```

### File Structure

```
day_46_spotify_playlist/
├── main.py              # Main application script
├── .env                 # Environment variables (create this)
├── .cache-spotify       # Spotify auth cache (auto-generated)
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `SPOTIFY_CLIENT_ID` | Your Spotify app client ID | `abc123def456` |
| `SPOTIFY_CLIENT_SECRET` | Your Spotify app client secret | `xyz789uvw012` |
| `SPOTIFY_REDIRECT_URI` | OAuth redirect URI | `http://localhost:8080` |

### Spotify Scopes
- `playlist-modify-private`: Create and modify private playlists

## 🎯 Features in Detail

### Billboard Scraping
- **Date Flexibility**: Works with any date from Billboard's available history
- **Data Extraction**: Retrieves both song titles and artist names
- **Filtering**: Removes invalid entries and duplicates
- **Error Handling**: Manages network errors and invalid responses

### Spotify Integration
- **OAuth 2.0**: Secure authentication flow
- **Search Optimization**: Combines song and artist for better matching
- **Playlist Management**: Creates private playlists with metadata
- **Batch Operations**: Efficiently adds multiple tracks

### Error Handling
- **Missing Songs**: Reports songs not found on Spotify
- **API Errors**: Handles Spotify API rate limits and errors
- **Network Issues**: Manages connection problems gracefully
- **Authentication**: Clear error messages for auth failures

## 🐛 Troubleshooting

### Common Issues

#### 1. Authentication Problems
```
Error: Unable to authenticate with Spotify API
```
**Solutions:**
- Check your `.env` file credentials
- Verify redirect URI matches Spotify app settings
- Ensure you have internet connection
- Try deleting `.cache-spotify` file and re-authenticating

#### 2. No Songs Found
```
Song not found on Spotify: [Song Name] by [Artist]
```
**Reasons:**
- Song not available on Spotify
- Different spelling/formatting between Billboard and Spotify
- Regional availability restrictions
- Artist name variations

#### 3. Billboard Scraping Issues
```
Error: 404 or connection timeout
```
**Solutions:**
- Check date format (YYYY-MM-DD)
- Verify date exists in Billboard history
- Check internet connection
- Billboard.com might be temporarily unavailable

#### 4. Empty Playlist
```
No songs found to add to the playlist
```
**Causes:**
- All songs failed to match on Spotify
- Billboard page structure changed
- Network issues during scraping

## 🔒 Security & Privacy

### Data Handling
- **No Data Storage**: Song data is processed in memory only
- **Temporary Cache**: Spotify auth tokens cached locally
- **Private Playlists**: All created playlists are private by default
- **Environment Variables**: Sensitive credentials stored securely

### API Limits
- **Spotify Rate Limits**: Respects Spotify's API rate limits
- **Billboard Scraping**: Uses appropriate delays between requests
- **Error Recovery**: Implements retry logic for failed requests

## 🚀 Advanced Usage

### Batch Processing
Create multiple playlists for different years:

```python
years = ["2020-01-01", "2019-01-01", "2018-01-01"]
for year in years:
    # Run the main logic for each year
```

### Custom Playlist Names
Modify the playlist naming convention:

```python
playlist_name = f"My {year.split('-')[0]} Throwback Hits"
```

### Song Filtering
Add custom filtering logic:

```python
# Only add songs from specific genres
if 'rock' in song_genre.lower():
    song_uris.append(track_uri)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/

# Check code style
flake8 main.py
```

## 📈 Future Enhancements

- [ ] **GUI Interface**: Create a user-friendly graphical interface
- [ ] **Multiple Chart Sources**: Support for other music charts (UK Charts, etc.)
- [ ] **Playlist Management**: Edit existing playlists, merge playlists
- [ ] **Song Analytics**: Show statistics about found/missing songs
- [ ] **Batch Processing**: Process multiple dates at once
- [ ] **Custom Filters**: Filter by genre, popularity, or artist
- [ ] **Export Options**: Export playlist data to CSV/JSON
- [ ] **Collaborative Playlists**: Create public collaborative playlists
- [ ] **Song Recommendations**: Suggest similar songs for missing tracks
- [ ] **Historical Analysis**: Track chart changes over time

## 📝 License

This project is part of the "100 Days of Code: The Complete Python Pro Bootcamp" course. Feel free to use this code for educational and personal purposes.

## 🙏 Acknowledgments

- **Spotify Web API**: For providing access to music streaming data
- **Billboard.com**: For maintaining historical chart data
- **Beautiful Soup**: For making web scraping accessible
- **Spotipy**: For simplifying Spotify API interactions

## 📞 Support

If you encounter any issues:

1. Check the [Troubleshooting](#🐛-troubleshooting) section
2. Review your [Spotify API setup](#spotify-api-setup)
3. Verify your `.env` file configuration
4. Create an issue with detailed error messages

## 🎓 Learning Objectives

This project demonstrates:
- **Web Scraping**: Extracting data from websites using BeautifulSoup
- **API Integration**: Working with REST APIs and OAuth authentication
- **Data Processing**: Cleaning and matching data from different sources
- **Error Handling**: Robust error management in Python applications
- **Environment Management**: Secure credential storage and configuration
- **Third-party Libraries**: Effective use of Python packages

---

**Start your musical time travel today!** 🎶✨

*This project is part of Day 46 of the 100 Days of Code: The Complete Python Pro Bootcamp.*
