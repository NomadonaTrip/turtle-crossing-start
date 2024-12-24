import time
from turtle import Screen
from player import Player
from car_manager import CarManager, STARTING_MOVE_DISTANCE
from scoreboard import Scoreboard, FONT
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()

screen.tracer(0)
player = Player()
score = Scoreboard()
car_spawn = CarManager()


screen.update()
screen.onkeypress(fun=player.move, key="Up")


#turtle controls



game_is_on = True
# count = 0
random_chance = random.randint(1,8)
while game_is_on:

    time.sleep(0.1)
    screen.update()
    car_spawn.create_car()
    car_spawn.move()
    for car in car_spawn.car_list:
        if player.ycor() > 300:
            player.goto(x=0, y=-300)
            car_spawn.next_level()
            score.level_up()
        if player.distance(car) < 20:
            score.end_game()
            game_is_on = False




    # game_is_on = False



screen.exitonclick()