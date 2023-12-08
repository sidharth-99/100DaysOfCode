import turtle as t
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(height=600, width=800)
screen.title("My Ping Pong Game")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
screen.tracer(0)
ball = Ball()
r_scoreboard = Scoreboard(300,260)
l_scoreboard = Scoreboard(-300,260)
# screen.update()
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# screen.update()

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update() # After initial initialization this is needed to update the display 
    ball.move()

    if ball.ycor()<=-280 or ball.ycor()>=280:
        # time.sleep(0.11)
        ball.bounce()
    
    if (l_paddle.distance(ball)<40 and l_paddle.xcor()<-340) or (r_paddle.distance(ball)<40 and r_paddle.xcor()>340):
        ball.bounce_paddle()
    
    if ball.xcor()<=-400:
        # time.sleep(0.11)
        r_scoreboard.score_update()
        ball.reset()
        # l_scoreboard.gameover()

    if ball.xcor()>=400:
        # time.sleep(0.11)
        l_scoreboard.score_update()
        ball.reset()
        # r_scoreboard.gameover()
        
screen.exitonclick()