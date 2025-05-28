"""
This module implements a simple "Higher-Lower" number guessing game using Flask.
Modules:
    - random: For generating random numbers.
    - flask: For creating the web application.
    - style_text: Contains the Stalying class for styling HTML responses.
Global Variables:
    - number (int): The current random number to be guessed, between 0 and 9.
Decorators:
    - generate_random_number: Regenerates the random number each time the decorated function is called.
    - Stalying.bold, Stalying.underline, Stalying.center: Style the HTML output of the home route.
Flask Routes:
    - '/': Home page. Welcomes the user and prompts to guess a number.
    - '/higher': Informs the user to guess a higher number.
    - '/lower': Informs the user to guess a lower number.
    - '/guess/<int:guess>': Checks the user's guess and responds accordingly.
Usage:
    Run this script to start the Flask web server and play the game in a browser.
"""
import random
from flask import Flask
from style_text import Stalying

app = Flask(__name__)
global number
number = random.randint(0, 9)

def generate_random_number(func):
    def wrapper(*args, **kwargs):
        global number
        number = random.randint(0, 9)
        print(f"Random number generated: {number}")
        return func(*args, **kwargs)
    return wrapper

@app.route('/')
@Stalying.bold
#@Stalying.italic
@Stalying.underline
@Stalying.center
@generate_random_number
def home():
    return "<h1>Welcome to the Higher-Lower Game!</h1>" \
    "<p>Guess a number between 0 and 9.</p>" \
    "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='Number Guessing Game'>"



@app.route('/higher')
def higher():
    return "<h1>Higher!</h1>" \
           "<p>Try again with a higher number.</p>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='Higher'>"
@app.route('/lower')
def lower():
    return "<h1>Lower!</h1>" \
           "<p>Try again with a lower number.</p>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='Lower'>"

@app.route('/guess/<int:guess>')
def main(guess):
    print(f"User guessed: {guess}")
    if guess < number:
        return higher()
    elif guess > number:
        return lower()
    else:
        return "<h1>Congratulations! You guessed the number!</h1>" \
               "<p>Play again!</p>" \
               "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='Congratulations'>"
    
if __name__ == '__main__':
    app.run(debug=True)
