from turtle import Screen
import time
from constants import (
    SCREEN_HEIGHT, SCREEN_WIDTH,
    SCREEN_UPDATE_TIME
)

screen = Screen()
screen.bgcolor("black")
screen.title("Turtle Crossing Game")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(SCREEN_UPDATE_TIME)

screen.exitonclick()
