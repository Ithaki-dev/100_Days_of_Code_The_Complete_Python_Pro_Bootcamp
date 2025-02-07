#This program is a encyper and decrypter for the Caesar cipher
import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)



def caesar_cipher(text, shift, direction):
    new_text = ""
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            if direction == "encode":
                new_index = index + shift
            elif direction == "decode":
                new_index = index - shift
            new_index = new_index % 26
            new_text += alphabet[new_index]
        else:
            new_text += letter
    print(f"The {direction}d text is: {new_text}")

user_choice = "yes"
while user_choice == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")  
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar_cipher(text, shift, direction)
    user_choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")