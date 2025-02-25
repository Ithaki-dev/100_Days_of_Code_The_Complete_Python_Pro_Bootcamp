#this is the class ball

from turtle import Turtle, Screen

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(1)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    def bounce_wall(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1

    def out_of_bounds(self):
        if self.xcor() > 380 or self.xcor() < -380:
            return True
        else:
            return False
