import random
from flask import Flask
from style_text import Stalying

app = Flask(__name__)

# Generate a random number between 0 and 9
def generate_random_number():
    """Generate a random number between 0 and 9."""
    return random.randint(0, 9)



@app.route('/')
@Stalying.bold
#@Stalying.italic
@Stalying.underline
@Stalying.center
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
def main(guess, number=generate_random_number()):
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
