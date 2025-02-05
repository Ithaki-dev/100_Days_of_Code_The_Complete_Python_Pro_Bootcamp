# Program to play rock-paper-scissors with the computer
import random

def play():
    user = input("Choice'r' for rock, 'p' for paper, 's' for scissors\n")
    assert user in ['r', 'p', 's'], "Invalid choice"
    computer = random.choice(['r', 'p', 's'])

    if user == computer:

        print("Computer chose", computer)
        return 'It\'s a tie'

    if is_win(user, computer) == True:
        print("Computer chose", computer)
        return 'You won!'
    else:
        print("Computer chose", computer)
        return 'You lost!'

# return true if the player beats the opponent
# winning conditions: r > s, s > p, p > r
def is_win(user, computer):
    
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        if user == 'r':
            print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
      
""")
        elif user == 's':
            print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        else:
            print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")            
        return True
    return False

print(play())