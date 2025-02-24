#this is the paddle clas for the game

import turtle

class Paddle(turtle.Turtle):
    def __init__(self, side):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        if side == "left":
            self.goto(-350, 0)
        else:
            self.goto(350, 0)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.speed(0)
        self.setheading(90)
        
    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        
    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)