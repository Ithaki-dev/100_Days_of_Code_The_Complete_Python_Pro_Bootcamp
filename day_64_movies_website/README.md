# Movie Collection App

A simple web application to manage your favorite movies, built with Python, Flask, SQLAlchemy, and TMDB API.

## Features

- Add, edit, and delete movies from your collection
- Search for movies using the TMDB API
- View movie details including year, description, rating, and poster
- Rate and review your movies
- Responsive and user-friendly interface

## Technologies Used

- Python 3
- Flask
- SQLAlchemy (SQLite database)
- TMDB API
- HTML/CSS (Jinja2 templates)
- Bootstrap (optional for styling)

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/movie-collection-app.git
   cd movie-collection-app
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up your TMDB API key:**
   - Sign up at [TMDB](https://www.themoviedb.org/) and get your API key.
   - Add your API key to your environment variables or directly in the code (not recommended for production).

5. **Run the application:**
   ```
   python app.py
   ```

6. **Open your browser and go to:**
   ```
   http://127.0.0.1:5000/
   ```

## Project Structure

```
movie-collection-app/
│
├── app.py
├── requirements.txt
├── templates/
│   ├── list.html
│   ├── edit.html
│   └── ...
├── static/
│   └── ...
└── README.md
```

## License

This project is licensed under the MIT License.

---

**Enjoy managing your movie collection!**