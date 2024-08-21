from turtle import Screen
import time
from player import Player
from constants import (
    SCREEN_HEIGHT, SCREEN_WIDTH,
    SCREEN_UPDATE_TIME,
    SCREEN_BACKGROUND_COLOR,
    TURTLE_UP_KEY, TURTLE_Y_COR_BOUNDARY
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
loop_count = 0
while is_game_on:
    screen.update()
    time.sleep(SCREEN_UPDATE_TIME)

    if loop_count % 6 == 0:
        car_manager.generate_car()

    car_manager.move_cars()

    if player.ycor() >= TURTLE_Y_COR_BOUNDARY:
        scoreboard.increase_level()
        player.reset_player()
        car_manager.update_speed()

    loop_count += 1

screen.exitonclick()
