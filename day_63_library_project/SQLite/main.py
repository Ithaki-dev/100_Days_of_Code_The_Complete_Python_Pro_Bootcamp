# import sqlite3
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
# # Ensure the database file is created in the current directory
# db = sqlite3.connect(os.path.join(current_directory, "books-collection.db"))
# cursor = db.cursor()

# def create_table():
#     cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#     db.commit()

# if __name__ == "__main__":
#     # create_table()
#     # print("Table created successfully.")
#     cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
#     db.commit()
#     db.close()

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)
# Configure the SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(current_directory, "new-books-collection.db")
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

with app.app_context():
    # Create the database and tables
    #db.create_all()
    db.session.add(Book(title="Harry Potter", author="J. K. Rowling", rating=9.3))
    db.session.commit()

