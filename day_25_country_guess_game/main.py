import turtle
import pandas
import os

# Set up the screen
current_path = os.path.dirname(__file__)
screen = turtle.Screen()
screen.title("U.S. States Game")
image = current_path + "\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load the state data
data = pandas.read_csv(current_path +"\\50_states.csv")

# Create a dictionary to hold the state names and their coordinates
states = data.state.to_list()
states_dict = {row.state: (row.x, row.y) for (index, row) in data.iterrows()}

# Create a list to hold the guessed states
guessed_states = []

# Read the missing state
missed_states_df = pandas.read_csv(current_path + "\\missed_states.csv", header=None)
missed_states = missed_states_df[1].to_list()

# Check guessed states
for state in states:
    if state not in missed_states:
        guessed_states.append(state)

#Show guessed states
try:
    for state in guessed_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(states_dict[state])
        t.write(state.capitalize(), align="center", font=("Arial", 8, "normal"))
except KeyError:
    pass

# Get the user's guess
user_guess = screen.textinput(f"Guess a State {len(guessed_states)} / {len(states)} ", "Enter the name of a state: ").title()

# Save the states that were not guessed
def save_game():
    missed_states = [state for state in states if state not in guessed_states]
    missed_states_df = pandas.DataFrame(missed_states)
    missed_states_df.to_csv(current_path + "\\missed_states.csv")

# Create a state marker when the user guesses the state correctly
def create_state():
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(states_dict[user_guess])
    t.write(user_guess.capitalize(), align="center", font=("Arial", 8, "normal"))

# Check if user's guess is correct
def game(user_guess):
    for state in guessed_states:
        if user_guess == state:
            create_state()
    while user_guess != "Exit":
        if user_guess in states_dict:
            guessed_states.append(user_guess)
            create_state()
            
        user_guess = screen.textinput(f"Guess a State {len(guessed_states)} / {len(states)} ", "Enter the name of a state: ").title()
        if user_guess == "Exit":
            save_game()
            break
        if len(guessed_states) == len(states):
            screen.bye()
            print("You have guessed all the states")
            break

if __name__ == "__main__":
    game(user_guess)
   


