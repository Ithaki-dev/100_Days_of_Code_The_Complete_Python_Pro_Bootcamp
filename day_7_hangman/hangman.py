#This is a fun Hangman game that you can play in the terminal.
import hangman_arts, hangman_words
from nltk.corpus import words
         
def play():
    chosen_word = hangman_words.get_word(words)
    placeholder = ""
    print(hangman_arts.logo)
    for position in range(len(chosen_word)):
        placeholder += "_"
    print(placeholder)

    game_over = False
    correct_letters = []
    lives = 6

    while not game_over:
        guess = input("Guess a letter: ").lower() 
        if guess in correct_letters:
            print(f"You've already guessed {guess}")
            continue
        display = ""

        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        if guess not in chosen_word:
            lives -= 1
            print(f"{guess} is not in the word. You lose a life.")

        print(display)      
        print(f"Lives: {lives}")
        print(hangman_arts.stages[lives])

        if "_" not in display:
            game_over = True
            print("You win!") 
        elif lives == 0:
            game_over = True
            print("You lose!")


