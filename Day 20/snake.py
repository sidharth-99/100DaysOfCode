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
        self.head = self.segments[0] 
        
    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            newx = self.segments[i-1].xcor()
            newy = self.segments[i-1].ycor()
            self.segments[i].goto(newx,newy)
    
        self.head.forward(20)

    def grow(self):
        seg = t.Turtle(shape = "square")
        seg.color("white")
        seg.penup()
        newx = self.segments[len(self.segments)-1].xcor()
        newy = self.segments[len(self.segments)-1].ycor()
        #Insted of xcor and ycor can also use position, refer ipynb file
        seg.goto(newx,newy)
        self.segments.append(seg)

    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
        
    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)
    
    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)