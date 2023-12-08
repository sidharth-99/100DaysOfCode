import turtle as t

class Paddle(t.Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.goto(x, y)
     
    def up(self):
        new_y = self.ycor() + 20 
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20 
        self.goto(self.xcor(), new_y)