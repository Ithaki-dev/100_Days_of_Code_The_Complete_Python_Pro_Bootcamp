#check the word recived from user and return the NATO alphabetic words

import pandas
import os

current_path = os.path.dirname(__file__)

# load the NATO alphabet
nato_data = pandas.read_csv(current_path + '\\nato_phonetic_alphabet.csv')

#create a list of the phonetic code words from a word that the user inputs
def convert_to_nato(word):
    # using list comprehension
    nato_words = [nato_data.loc[nato_data['letter'] == letter, 'code'].iloc[0] for letter in word.upper()]
    
    return nato_words


word=""
# test the function
while True:
    word = input("Enter a word: ")
    print("Enter 'quit' to exit.")
    if word.lower() == 'quit':
        break
    # catch if the input is not a letter
    try:
        if not word.isalpha():
            raise ValueError("Input should be a letter")
    except ValueError as e:
        print(e)
    else:
        nato_words = convert_to_nato(word)
        print(nato_words)


