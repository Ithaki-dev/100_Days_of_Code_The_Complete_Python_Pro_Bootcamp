#this is the class score
from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center",
                    font=("Courier", 24, "normal"))
        
    def increase_score(self):
        self.score += 1
        self.update_score()