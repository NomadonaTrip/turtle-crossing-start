import time
from turtle import Screen
from player import Player
from car_manager import CarManager, STARTING_MOVE_DISTANCE
from scoreboard import Scoreboard, FONT

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()

screen.tracer(0)
player = Player()
score = Scoreboard()


screen.update()
screen.onkeypress(fun=player.move, key="Up")


#turtle controls



game_is_on = True
count = 0
car_list = []
while game_is_on:
    count += 1
    if count % 223:
        car_1 = CarManager()
        car_list.append(car_1)
    for car in car_list:
        car.move()
        # if car.xcor() < -300:
        #     car.goto(x = 300, y = 0)
        if player.ycor() > 300:
            player.goto(x=0, y=-300)
            car.next_level()
            score.level_up()
        if player.distance(car) < 20:
            score.end_game()
            game_is_on = False

    time.sleep(0.1)
    screen.update()


    # game_is_on = False



screen.exitonclick()