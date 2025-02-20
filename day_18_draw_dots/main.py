# This is a program for creating dots paints

import random
from turtle import Turtle, Screen


bobby = Turtle()
bobby.shape("circle")
color_list = ["black", "red", "green", "yellow", "blue", "brown", "orange", "purple"]

def drawShape(num):
    bobby.color(random.choice(color_list))
    for _ in range(num):
        bobby.forward(100)
        bobby.right(360/num)

for i in range(3,11):
    drawShape(i)
    


screen = Screen()
screen.exitonclick()
