# This is the class for creating cars in the frog game
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"] 
import time
from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(300, random.randint(-225, 225))
        self.setheading(180)
        self.speed = 5
        

    def move(self):
        self.forward(self.speed)
        

    def reset_position(self):
        self.goto(300, random.randint(-250, 250))
        

    def increase_speed(self):
        self.speed += 2
        self.move()

    def reset_speed(self):
        self.speed = 5
        self.move()