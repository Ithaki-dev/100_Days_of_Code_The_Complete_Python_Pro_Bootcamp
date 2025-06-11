from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
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
# Configure the SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(current_directory, "SQLite/new-books-collection.db")
# Disable track modifications to save memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = 'books'
    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String(250), nullable=False)
    author = mapped_column(String(250), nullable=False)
    rating = mapped_column(Float, nullable=False)

all_books = []


@app.route('/')
def home():
    with app.app_context():
        # Query all books from the database
        all_books = db.session.query(Book).all()
        # Convert the SQLAlchemy objects to dictionaries for rendering
        all_books = [{"title": book.title, "author": book.author, "rating": book.rating} for book in all_books]
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book_title = request.form["title"]
        book_author = request.form["author"]
        book_rating = request.form["rating"]
        all_books.append({"title": book_title, "author": book_author , "rating": book_rating})
        print(all_books)
        with app.app_context():
            new_book = Book(title=book_title, author=book_author, rating=float(book_rating))
            db.session.add(new_book)
            db.session.commit()
        # Redirect to the home page after adding the book
        return redirect(url_for("home"))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

