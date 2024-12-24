import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len= 2)
        self.penup()
        self.goto(x = 290, y = random.randint(-250, 250))
        self.color(random.choice(COLORS))
        self.speed = STARTING_MOVE_DISTANCE

    def move(self):
        self.backward(self.speed)

    def next_level(self):
        self.speed += MOVE_INCREMENT



