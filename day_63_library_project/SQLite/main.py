import sqlite3
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
# Ensure the database file is created in the current directory
db = sqlite3.connect(os.path.join(current_directory, "books-collection.db"))
cursor = db.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
    db.commit()

if __name__ == "__main__":
    # create_table()
    # print("Table created successfully.")
    cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
    db.commit()
    db.close()