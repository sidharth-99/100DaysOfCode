import turtle as t

tim = t.Turtle()
screen = t.Screen()

def move():
    tim.forward(100)

screen.listen()
screen.onkey(key="space", fun=move)

screen.exitonclick()#screen doesn't disapper after running