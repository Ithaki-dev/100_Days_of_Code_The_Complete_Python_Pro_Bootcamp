from turtle import Turtle, Screen

bobby = Turtle()
screen = Screen()

def move_forward():
    bobby.forward(100)

bobby.teleport(-215,-215)
screen.listen()
screen.onkey(move_forward,"w")

screen.exitonclick()