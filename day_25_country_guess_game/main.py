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
states_dict = {state: (data.x[data.state == state].values[0], data.y[data.state == state].values[0]) for state in states}

# Create a turtle for each state
state_turtles = []
for state in states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(states_dict[state])
    t.write(state)
    state_turtles.append(t)
    t.onclick(lambda state=state: check_answer(state))
    t.speed(0)
    t.showturtle()

screen.exitonclick()
