
import colorgram
import os
import turtle as t
import random

# relative_path = os.path.join('day_18_draw_dots', 'image.jpg')#-
# colors = colorgram.extract(relative_path,30)#-
# rgb_colors = []#-
#-
#this method is for extracting colors from an image#-
# for color in colors:#-
#     r = color.rgb.r#-
#     g = color.rgb.g#-
#     b = color.rgb.b#-
#     new_color = (r,g,b)#-
#     rgb_colors.append(new_color)#-

color_list = [
    (245, 239, 230), (251, 226, 233), (46, 92, 144), (243, 250, 245), 
    (170, 13, 26), (34, 44, 62), (141, 80, 44), (228, 154, 7), 
    (161, 57, 88), (211, 162, 101), (37, 144, 46), (68, 34, 47), 
    (235, 219, 63), (225, 223, 4), (48, 45, 93), (22, 51, 47), 
    (50, 40, 36), (88, 195, 171), (117, 162, 171), (247, 90, 16), 
    (18, 96, 49), (233, 237, 244), (211, 56, 76), (155, 23, 19), 
    (187, 143, 156), (60, 167, 91), (46, 149, 196), (226, 177, 167), 
    (163, 209, 182), (227, 171, 180)
]


# Set up the screen
screen = t.Screen()
screen.setup(width=500, height=500)
screen.colormode(255)

# Create the turtle
dot_maker = t.Turtle()
dot_maker.hideturtle()
dot_maker.penup()

# Painting parameters
dot_size = 20
dot_spacing = 50
num_rows = 10
num_cols = 10

def draw_hirst_painting():
    # Start position (bottom-left corner)
    start_x = -225
    start_y = -225

    for row in range(num_rows):
        for col in range(num_cols):
            # Move to the next dot position
            dot_maker.goto(start_x + col * dot_spacing, start_y + row * dot_spacing)

            # Choose a random color from the color list
            color = random.choice(color_list)

            # Draw the dot
            dot_maker.dot(dot_size, color)

# Call the function to draw the painting
draw_hirst_painting()

# Exit on click
screen.exitonclick()




