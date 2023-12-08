import turtle as t
import random

class Scoreboard(t.Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.penup()
        self.score=0
        self.color('white')
        self.goto(x,y)
        self.write(f'Score :{self.score}', move=False, align='center', font=('Arial', 24, 'normal'))
        self.hideturtle()

    def gameover(self):
        self.goto(0,0)
        self.write('GAME OVER', move=False, align='center', font=('Arial', 40, 'normal'))
        
    def score_update(self):
        self.score+=1
        self.clear()
        self.write(f'Score :{self.score}', move=False, align='center', font=('Arial', 24, 'normal'))
