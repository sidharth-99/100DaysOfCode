import turtle as t
FONT = ("Courier", 24, "normal")

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level=0
        self.goto(-200,260)
        self.write(f'Level :{self.level}', move=False, align='center', font=FONT)
        self.hideturtle()

    def gameover(self):
        self.goto(0,0)
        self.write('GAME OVER', move=False, align='center', font=FONT)
        
    def level_update(self):
        self.level+=1
        self.clear()
        self.write(f'Level :{self.level}', move=False, align='center', font=FONT)
