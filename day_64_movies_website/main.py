
"""
A Flask web application for managing a personal movie collection using a SQLite database.
Features include adding, editing, deleting, and displaying movies, as well as searching for movies using The Movie Database (TMDB) API.
Modules and Libraries:
- Flask: Web framework for routing and rendering templates.
- Flask-Bootstrap: For integrating Bootstrap styles.
- Flask-SQLAlchemy: ORM for database management.
- SQLAlchemy: Database schema definitions.
- Flask-WTF & WTForms: For form handling and validation.
- Requests: For making HTTP requests to TMDB API.
- OS: For file path management.
Configuration:
- Uses a SQLite database stored in the 'instance' directory.
- Requires TMDB API key and access token for movie search functionality.
Database Model:
- Movie: Stores movie details such as title, year, description, rating, ranking, review, and image URL.
Forms:
- MovieForm: For editing movie details.
- AddMovieForm: For searching and adding new movies.
Routes:
- '/' (home): Displays all movies in the database.
- '/edit/<int:movie_id>': Edit details of a specific movie.
- '/delete/<int:movie_id>': Delete a movie from the database.
- '/add': Search for a movie by title using TMDB API and select from results.
- '/find/<movie_id>': Fetches movie details from TMDB and adds it to the database.
Usage:
- Run the script to start the Flask development server.
- Access the web interface to manage the movie collection.
Note:
- Replace 'your_access_token_here' and 'your_api_key_here' with valid TMDB credentials.
"""
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os
current_directory = os.path.dirname(os.path.abspath(__file__))



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# API URL and headers for The Movie Database (TMDB)
url = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"
access_token = "your_access_token_here"  # Replace with your actual access token
headers = {
    "accept": "application/json",
    "Authorization": "Bearer " + access_token
}

# CREATE DB
# Configure the SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(current_directory, "instance/Movie.db")
# Disable track modifications to save memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

# CREATE TABLE
class Movie(db.Model):
    __tablename__ = 'movies'
    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String(250), nullable=False)
    year = mapped_column(Integer, nullable=False)
    description = mapped_column(String(500), nullable=False)
    rating = mapped_column(Float, nullable=False)
    ranking = mapped_column(Integer, nullable=False)
    review = mapped_column(String(500), nullable=True)
    img_url = mapped_column(String(500), nullable=False)
# Create the database and tables if they don't exist
# with app.app_context():
#     db.create_all()

class MovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    year = StringField("Year", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    rating = StringField("Rating", validators=[DataRequired()])
    ranking = StringField("Ranking", validators=[DataRequired()])
    review = StringField("Review")
    img_url = StringField("Image URL", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    with app.app_context():
        # Query all movies from the database
        all_movies = db.session.query(Movie).order_by(Movie.rating.desc()).all()
        # Convert the SQLAlchemy objects to dictionaries for rendering
        all_movies = [{"title": movie.title, "year": movie.year, "description": movie.description,
                       "rating": movie.rating, "ranking": movie.ranking, "review": movie.review,
                       "img_url": movie.img_url, "id": movie.id} for movie in all_movies]
    return render_template("index.html", movies=all_movies)

@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit_movie(movie_id):
    with app.app_context():
        movie = db.session.query(Movie).filter(Movie.id == movie_id).first()
        form = MovieForm(obj=movie)
        if form.validate_on_submit():
            form.populate_obj(movie)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("edit.html", form=form)

@app.route("/delete/<int:movie_id>")
def delete_movie(movie_id):
    with app.app_context():
        movie_to_delete = db.session.query(Movie).filter(Movie.id == movie_id).first()
        if movie_to_delete:
            db.session.delete(movie_to_delete)
            db.session.commit()
    return redirect(url_for("home"))

@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        params = {
            "query": movie_title,
            "include_adult": "false",
            "language": "en-US",
            "page": 1
        }
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        movies = data.get("results", [])
        if movies:
            return render_template("select.html", movies=movies)
        else:
            return print("No movies found with that title.")
    return render_template("add.html", form=form)

@app.route("/find/<movie_id>")
def find_movie(movie_id):
    print(movie_id)
    if movie_id:
        movie_api_url = f'https://api.themoviedb.org/3/movie/{movie_id}'
        response = requests.get(movie_api_url, headers=headers)
        data = response.json()
        new_movie = Movie(
            id=data["id"],
            title=data["title"],
            year=data["release_date"].split("-")[0],
            rating=data["vote_average"],
            ranking=0,  # Default ranking, can be updated later
            review="",  # Default review, can be updated later
            img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
            description=data["overview"]
        )
        # Add the new movie to the database
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit_movie", movie_id=new_movie.id))
    return "Movie not found", 404
    

if __name__ == '__main__':
    app.run(debug=True)
