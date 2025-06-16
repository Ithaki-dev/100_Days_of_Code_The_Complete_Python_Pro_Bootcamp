from pprint import pprint
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

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# API URL and headers for The Movie Database (TMDB)
url = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"
access_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmM2EwMThhNTZlYThmNDY0YTg4ZGM3OTM2N2NjNTQzMyIsIm5iZiI6MTc0OTkzNDU5OC43NzEwMDAxLCJzdWIiOiI2ODRkZTIwNmI1MThkZmRjYjIzZGY3YTMiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.jq4k49_6XxLzkSmxcRau9kK3zJ-9h9f8D28PQQnwqhw"
api_key = "f3a018a56ea8f464a88dc79367cc5433"
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
with app.app_context():
    db.create_all()
    #  Create a sample movie if the table is empty
#     second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )

#     db.session.add(second_movie)
#     db.session.commit()

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
        dictionary_movies = []
        # pprint(movies)
        # for movie in movies:
        #     new_movie = Movie(
        #         id=movie.get("id"),
        #         title=movie.get("title"),
        #         year=movie.get("release_date", "").split("-")[0] if movie.get("release_date") else "Unknown",
        #         description=movie.get("overview", "No description available."),
        #         rating=movie.get("vote_average", 0.0),
        #         ranking=0,  # Default ranking, can be updated later
        #         review="",  # Default review, can be updated later
        #         img_url=f"https://image.tmdb.org/t/p/w500{movie.get('poster_path', '')}"
        #     )
        #     # Add the movie to the dictionary list
        #     dictionary_movies.append(new_movie)


        #  Print the movie dictionary for debugging
        #pprint(movies)
        if movies:
            return render_template("select.html", movies=movies)
        else:
            return print("No movies found with that title.")
    return render_template("add.html", form=form)

@app.route("/find/<movie_id>")
def find_movie(movie_id):
    print(movie_id)
    if movie_id:
        movie_api_url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
        #The language parameter is optional, if you were making the website for a different audience
        #e.g. Hindi speakers then you might choose "hi-IN"
        response = requests.get(movie_api_url)
        data = response.json()
        pprint(data)
        new_movie = Movie(
            id=data["id"],
            title=data["title"],
            #The data in release_date includes month and day, we will want to get rid of.
            year=data["release_date"].split("-")[0],
            rating=data["vote_average"],
            ranking=0,  # Default ranking, can be updated later
            review="",  # Default review, can be updated later
            img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home"))
    return "Movie not found", 404
    



if __name__ == '__main__':
    app.run(debug=True)
