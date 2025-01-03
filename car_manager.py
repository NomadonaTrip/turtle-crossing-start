import random
from turtle import Turtle



COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):

        self.car_list = []
        self.speed = STARTING_MOVE_DISTANCE



    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            # self.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(x=290, y=random.randint(-250, 250))
            new_car.color(random.choice(COLORS))
            self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            car.backward(self.speed)

    def next_level(self):
        self.speed += MOVE_INCREMENT





