# program to guess the secret number >:)

import random

#Function for were we create the ramdom number for user to guess

def guess_number(x):
    ramdom_number = random.randint(1, x)
    guess = 0
    while guess != ramdom_number:
        guess = int(input(f"Guess the number between 1 to {x}: "))
        if guess > ramdom_number:
            print("Sorry, guess again. Too high")
        elif guess < ramdom_number:
            print("Sorry, guess again. Too low")
    print(f"Nice, correctly you guess the number {ramdom_number}")

guess_number(10)
