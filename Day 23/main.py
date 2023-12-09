import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
carmanager = CarManager()
screen.title("Turtle Crossing Game")
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_car()
    carmanager.move()
    for car in carmanager.all_cars:
        if car.distance(player)<20:
            scoreboard.gameover()
            game_is_on =False

    if player.reset()== True:
        scoreboard.level_update()
        carmanager.speed_update()
    

screen.exitonclick()