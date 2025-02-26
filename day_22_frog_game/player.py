# This class implements the player object for the frog game

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)
        self.color("green")

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)
        

    def reset_position(self):
        self.goto(0, -280)

    