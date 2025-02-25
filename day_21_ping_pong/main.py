# This is the famous game ping pong

from turtle import Screen,Turtle
from ball import Ball
from paddle import Paddle
import time
from score_board import Scoreboard

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

pladdle_player1 = Paddle(side="left")
pladdle_player2 = Paddle(side="right")
ball = Ball()
score = Scoreboard()



screen.listen()

screen.onkey(pladdle_player1.move_up, "w")
screen.onkey(pladdle_player1.move_down, "s")
screen.onkey(pladdle_player2.move_up, "Up")
screen.onkey(pladdle_player2.move_down, "Down")

game_on = True
while game_on:
    time.sleep(0.08)
    screen.update()
    #moving the ball
    ball.move()
    #bounce the ball
    ball.bounce_wall()
    #bounce the ball with the paddle
    if ball.distance(pladdle_player1) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()
    elif ball.distance(pladdle_player2) < 50 and ball.xcor() > 320:
        ball.bounce_paddle()

    #check if the ball is out of bounds
    if ball.out_of_bounds():
        if ball.xcor() > 380:
            ball.goto(0,0)
            ball.bounce_paddle()
            score.l_point()
        else:
            ball.goto(0,0)
            ball.bounce_paddle()
            score.r_point()


        

    

screen.exitonclick()