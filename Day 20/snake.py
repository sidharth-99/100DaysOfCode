import turtle as t
import time


class Snake():
    def __init__(self):
        self.segments = []
        x=0
        for i in range(3):
            seg = t.Turtle(shape = "square")
            seg.color("white")
            seg.penup()
            seg.goto(x,0)
            x-=20
            self.segments.append(seg)
    