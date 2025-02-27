#this is the class score
from turtle import Turtle
import os
CSV_FILE = "day_20_snake_game\high_score.csv"
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-125, 250)
        self.hideturtle()
        self.update_score()

        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center",
                    font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("Courier", 24, "normal"))
        self.hideturtle()
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def reset_score(self):
        self.score = 0
        self.update_score()

class HighScore(Turtle):
        def __init__(self):
            super().__init__()
            self.high_score = 0
            self.color("white")
            self.penup()
            self.goto(125, 250)
            self.hideturtle()
            self.check_if_high_score_exists()
            self.read_high_score()
            self.update_high_score()
            
        
            #this function checks if a high score exists 

        def check_if_high_score_exists(self):
            if not os.path.exists(CSV_FILE):
                with open(CSV_FILE, mode="w") as file:
                    file.write("0")
            self.read_high_score()

        def update_high_score(self):
            self.clear()
            self.write(f"High Score: {self.high_score}", align="center",
                        font=("Courier", 24, "normal")) 

        def write_high_score(self):
            with open(CSV_FILE, mode="w") as file:
                file.write(f"{self.high_score}")

        def read_high_score(self):
            with open(CSV_FILE, mode="r") as file:
                self.high_score = int(file.read())
            return self.high_score
    


    
