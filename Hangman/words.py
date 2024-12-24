#This is a fun Hangman game
import random
import string
from nltk.corpus import words


def get_word(words):
    word = random.choice(words.words())
    print(word)
    return word

def hangman():
    word = get_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    print(word_letters + alphabet)



hangman()