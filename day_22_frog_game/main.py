#this is the clasic foog path game

import time
from turtle import Screen, Turtle
from player import Player
from car_manager import Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
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


    # Create a new car every 6 iterations
    if counter % 6 == 0:
        new_car = Car()
        cars.append(new_car)
        if score.level > 1:
            new_car.increase_speed()

    # Move all cars
    for car in cars:
        car.move()

        #Remove cars that have gone off-screen
        if car.xcor() < -320:
            cars.remove(car)
            car.hideturtle()  # Hide the car from view
            del car  # Delete the car object
    counter += 1

    #Check for collision with player
    for car in cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()
            

    #check if the player reach the finish point
    if player.ycor() > 260:
        score.increase_level()
        player.reset_position()
        
        counter = 0
        # Remove all cars from the screen
        for car in cars:
            cars.remove(car)
            car.hideturtle()


screen.exitonclick()
