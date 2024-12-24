#This is a fun Hangman game
import random
import string
from nltk.corpus import words

#Function to get a word from the nltk corpus
def get_word(words):
    word = random.choice(words.words()).upper()
    print(word)
    return word

#Function to play the game
def hangman():
    word = get_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    #get the user input
    while len(word_letters) > 0:
        print("You have used these letters: ", " ".join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")
        else:
            print("Invalid character. Please try again.")
    print(word)
    print("Congratulations! You have guessed the word: ", word)



hangman()