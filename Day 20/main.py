import turtle as t
import time
from snake import Snake

screen = t.Screen()
screen.setup(height=600, width=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

segments = []
# snake =Snake()
x=0
for i in range(3):
    seg = t.Turtle(shape = "square")
    seg.color("white")
    seg.penup()
    seg.goto(x,0)
    x-=20
    segments.append(seg)
    # seg.speed('slowest')
screen.update()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for i in range(len(segments)-1,0,-1):
        newx = segments[i-1].xcor()
        newy = segments[i-1].ycor()
        segments[i].goto(newx,newy)
    
    segments[0].forward(20)

screen.exitonclick()