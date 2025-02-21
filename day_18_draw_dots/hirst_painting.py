import colorgram
import os

relative_path = os.path.join('day_18_draw_dots', 'image.jpg')
colors = colorgram.extract(relative_path,6)

print(colors)
