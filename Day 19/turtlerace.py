import turtle as t
import random


screen = t.Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title='Place a Bet', prompt='Which turtle will win the race?')
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat"]

y = -150
all_turtles = []
for i in range(6):
    new_turtle = t.Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    y+=60
    new_turtle.color(colors[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on =True

while is_race_on:
    for turtle in all_turtles:
        if(turtle.xcor()>230):
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f'Yes, {winning_color} winner')
            else:
                print(f'No, {winning_color} winner') 
        turtle.forward(random.randint(1,10))
screen.exitonclick()