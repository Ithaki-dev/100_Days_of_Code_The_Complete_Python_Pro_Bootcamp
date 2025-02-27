##this is the famous snake game
import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Score, HighScore


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
high_score = HighScore()


game_is_on = True

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
        if score.score > high_score.high_score:
            high_score.high_score = score.score
            high_score.update_high_score()
            high_score.write_high_score()

    #Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()   

    
screen.exitonclick()