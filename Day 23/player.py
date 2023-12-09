import turtle as t
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        # self.shapesize(0.5, 0.5)
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION) 
    
    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def reset(self):
        if self.ycor()>=FINISH_LINE_Y:
            self.goto(STARTING_POSITION)

            return True
        else: return False
    