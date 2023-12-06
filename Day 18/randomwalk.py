import turtle as t
import random

tim = t.Turtle()


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim.pensize(10)

def walk(tim):
    tim.forward(random.randint(0,100))
    turn = random.randint(0,1)
    if turn == 0:
        tim.left(90)
    else: tim.right(90)

# for shape_side_n in range(3, 10):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

while(True):
    tim.color(random.choice(colours))
    walk(tim)

#We can even randomize the color with random rgb values as input