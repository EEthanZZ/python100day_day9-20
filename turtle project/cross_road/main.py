import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.move, "w")
cars = CarManager()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.car_move()
    for i in cars.all_cars:
        if player.distance(i) < 20:
            game_is_on = False

    if player.next_game():
        player.go_to_start()
screen.exitonclick()