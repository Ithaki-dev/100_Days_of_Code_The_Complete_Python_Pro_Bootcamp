from turtle import Turtle,Screen
from prettytable import PrettyTable

bob = Turtle() # Create a turtle object
bob.shape("turtle") # Change the shape of the turtle
bob.color("DarkBlue") # Change the color of the turtle
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)

table = PrettyTable() # Create a table object
table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"]) # Add rows to the table
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
table.align = "l" # Align the text to the right
print(table) # Print the table


my_screen = Screen() # Create a screen object
my_screen.exitonclick() # Close the screen when clicked

