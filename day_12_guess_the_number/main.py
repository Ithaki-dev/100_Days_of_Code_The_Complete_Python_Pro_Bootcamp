#this program is a number guessing game
import random
import os
from art import logo
def main():
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess the number.")
    dificulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    difficulty_list = ["easy", "hard"]  
    if dificulty not in difficulty_list:
        print("Invalid difficulty. Please try again.")
        return
    if dificulty == "easy":
        attempts = 10
    elif dificulty == "hard":
        attempts = 5

    
    number = random.randint(1, 100)
    guess = 0
    while guess != number and attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Enter your guess: "))
        if guess < number:
            print("Too low! Try again.")
            attempts -= 1
        elif guess > number:
            print("Too high! Try again.")
            attempts -= 1 
        elif guess == number:
            print("Congratulations! You guessed the number.")
            print(f"The number was {number}.")

    #os.system("cls")
    #main()

if __name__ == "__main__":
    main()
