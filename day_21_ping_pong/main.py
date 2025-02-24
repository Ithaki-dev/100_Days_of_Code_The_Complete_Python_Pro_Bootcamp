# This is the famous game ping pong

from turtle import Screen,Turtle
from paddle import Paddle

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)

pladdle_player1 = Paddle(side="left")
pladdle_player2 = Paddle(side="right")

screen.listen()

screen.onkey(pladdle_player1.move_up, "w")
screen.onkey(pladdle_player1.move_down, "s")
screen.onkey(pladdle_player2.move_up, "Up")
screen.onkey(pladdle_player2.move_down, "Down")

screen.exitonclick()