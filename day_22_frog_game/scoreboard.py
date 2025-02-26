#This is the class for ther  scoreboard
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"      Level: {self.level}", align="center", font=("Courier", 20, "normal"))
    
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
        self.hideturtle()

        
    def reset_level(self):
        self.level = 1
        self.update_scoreboard()