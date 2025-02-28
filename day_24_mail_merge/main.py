#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import os
from pathlib import Path
import re

current_path = Path.cwd()
starting_letter_path = current_path / "day_24_mail_merge/Input/Letters/starting_letter.txt"
invited_names_path = current_path / "day_24_mail_merge/Input/Names/invited_names.txt"
ready_to_send_folder = current_path / "day_24_mail_merge/Output/ReadyToSend"

def read_invited_names():
    with open(invited_names_path, "r") as file:
        names = file.readlines()
        return names
        
def create_letter(name):
    with open(starting_letter_path, "r") as file:
        letter = file.read()
        letter = re.sub(r'\[name\]', name, letter)
        return letter
    
def save_letter(letter, name):
    with open(f"{ready_to_send_folder}/{name}.txt", "w") as file:
        file.write(letter)

def main():
    names = read_invited_names()
    for name in names:
        name = name.strip()
        letter = create_letter(name)
        save_letter(letter, name)

if __name__ == "__main__":
    main()