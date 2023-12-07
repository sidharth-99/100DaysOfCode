import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(height=600, width=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

segments = []
snake =Snake()
food = Food()
scoreboard = Scoreboard()

screen.update()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.score_update()
        snake.grow()
        
    if snake.head.xcor()<=-280 or snake.head.xcor()>=280 or snake.head.ycor()<=-280 or snake.head.xcor()>=280:
        game_is_on = False
        scoreboard.gameover()

    for segments in snake.segments[1::]:
        # if segments == snake.head:
        #     continue
        if snake.head.distance(segments)<10:
            game_is_on = False
            scoreboard.gameover()

screen.exitonclick()