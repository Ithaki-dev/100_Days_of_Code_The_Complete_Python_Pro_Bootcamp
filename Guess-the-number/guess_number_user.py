# This is a prgrom that allows the computer to guess the number the user is thinking of

import random

def guess_number(x):
    
    guess = 0
    while guess != x:
        guess = random.randint(1, x)
        if guess > x:
            print("Sorry PC, guess again. Too high")
        elif guess < x:
            print("Sorry PC, guess again. Too low")
    print(f"Nice, correctly you guess the number {x} smart PC")

user__number = int(input(f"Enter the number between 1 to 10: "))
guess_number(user__number)