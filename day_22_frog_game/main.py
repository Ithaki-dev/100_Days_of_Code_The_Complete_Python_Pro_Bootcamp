#this is the clasic foog path game

import time
from turtle import Screen, Turtle
from player import Player
from car_manager import Car
# from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
counter = 0
cars = []  # List to store all cars

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # Move the player
    screen.listen()
    screen.onkey(player.move_up, "w")
    screen.onkey(player.move_down, "s")


    # Create a new car every 6 iterations#+
    if counter % 6 == 0:
        new_car = Car()
        cars.append(new_car)

    # Move all cars
    for car in cars:
        car.move()

        #Remove cars that have gone off-screen
        if car.xcor() < -320:
            cars.remove(car)
            car.hideturtle()  # Hide the car from view
            del car  # Delete the car object#+
    counter += 1

    #Check for collision with player
    for car in cars:
        if car.distance(player) < 40:
            game_is_on = False
            print("Game Over!")
screen.exitonclick()
