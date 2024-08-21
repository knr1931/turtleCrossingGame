import random
from turtle import Screen
import time
from player import Player
from constants import (
    SCREEN_HEIGHT, SCREEN_WIDTH,
    SCREEN_UPDATE_TIME,
    SCREEN_BACKGROUND_COLOR,
    TURTLE_UP_KEY, TURTLE_Y_COR_BOUNDARY,
    CAR_PLAYER_COLLISION_DISTANCE
)
from scoreboard import ScoreBoard
from car_manager import CarManager

screen = Screen()
screen.bgcolor(SCREEN_BACKGROUND_COLOR)
screen.title("Turtle Crossing Game")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

screen.listen()

player = Player()
screen.onkey(key=TURTLE_UP_KEY, fun=player.move)

car_manager = CarManager()

scoreboard = ScoreBoard()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(SCREEN_UPDATE_TIME)

    if random.randint(1, 6) == 1:
        car_manager.generate_car()

    car_manager.move_cars()

    # Detection of collision with the car
    for car in car_manager.cars:
        if car.distance(player) <= CAR_PLAYER_COLLISION_DISTANCE:
            is_game_on = False
            scoreboard.game_over()

    if player.ycor() >= TURTLE_Y_COR_BOUNDARY:
        scoreboard.increase_level()
        player.reset_player()
        car_manager.update_speed()

screen.exitonclick()
