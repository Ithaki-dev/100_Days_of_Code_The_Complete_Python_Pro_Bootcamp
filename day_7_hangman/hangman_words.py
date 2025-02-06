import random
from nltk.corpus import words

def get_word(words):
    word = random.choice(words.words()).lower()
    return word