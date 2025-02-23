from turtle import Turtle, Screen

bobby = Turtle()
screen = Screen()

key = " "

def move_forward(): 
    bobby.forward(50)

def move_backward():
    bobby.backward(50)

def turn_left():
    bobby.left(10)

def turn_right():
    bobby.right(10)

def clear():
    bobby.clear()
    bobby.penup()
    bobby.home()

screen.listen()
screen.onkey(move_backward,"s")
screen.onkey(move_forward,"w")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear,"c")

screen.exitonclick()