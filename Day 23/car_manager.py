import turtle as t
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(t.Turtle):
    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1,6)
        if chance==1:
            new_car = t.Turtle("square")
            new_car.shapesize(2, 1)
            new_car.color(random.choice(COLORS))
            new_car.setheading(90)
            new_car.penup()
            new_car.goto(320,random.randint(-260,260))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.move_speed 
            car.goto(new_x, car.ycor())

    def speed_update(self):
        self.move_speed += MOVE_INCREMENT
