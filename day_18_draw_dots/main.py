# This is a program for creating dots paints

import random
import turtle as t
from turtle import Turtle, Screen


bobby = Turtle()
bobby.shape("arrow")
bobby.pensize(3)
bobby.speed("fastest")
t.colormode(255)


color_list = ["black", "red", "green", "yellow", "blue", "brown", "orange", "purple"]
direction = [0,90,180,270]
def drawShape(num):
    bobby.color(random.choice(color_list))
    angle = 360 / num
    for _ in range(num):
        bobby.forward(100)
        bobby.right(angle)

def randomColor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def circle():
    bobby.color(randomColor())
    bobby.circle(200)



def randomWalk(num):
    for _ in range(num):
        bobby.color(randomColor())
        bobby.forward(30)
        bobby.setheading(random.choice(direction))
        

#for i in range(3,11):
#   drawShape(i)
#print(randomColor())
#randomWalk(100)
for i in range(100):
    circle()
    bobby.left(5)
    


screen = Screen()
screen.exitonclick()
