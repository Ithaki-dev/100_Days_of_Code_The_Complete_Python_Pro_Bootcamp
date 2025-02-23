import random
from turtle import Turtle, Screen

#bobby = Turtle(shape="turtle")
screen = Screen()
screen.setup(width=500, height= 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")
color_list = ["red", "green", "blue", "yellow", "brown","black"]
is_race_on = False
all_turtles = []

for color in color_list:
    b = Turtle()
    b.color(color)
    b.shape("turtle")
    b.penup()
    b.goto(-200, 100 - (color_list.index(color) * 40))
    all_turtles.append(b)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        rand_distance = random.randint(0,15)
        turtle.forward(rand_distance)
        if turtle.xcor() > 200:
            is_race_on = False
            winning_color = turtle.color()
            if winning_color[0] == user_bet:
                print(f"You've won! The {winning_color[0]} turtle won the race.")
                break
            else:
                print(f"You've lost! The {winning_color[0]} turtle won the race.")
                break
            
screen.exitonclick()
