from turtle import Screen
import time
from player import Player
from constants import (
    SCREEN_HEIGHT, SCREEN_WIDTH,
    SCREEN_UPDATE_TIME,
    SCREEN_BACKGROUND_COLOR,
    TURTLE_UP_KEY, TURTLE_Y_COR_BOUNDARY
)

screen = Screen()
screen.bgcolor(SCREEN_BACKGROUND_COLOR)
screen.title("Turtle Crossing Game")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

screen.listen()

player = Player()
screen.onkey(key=TURTLE_UP_KEY, fun=player.move)

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(SCREEN_UPDATE_TIME)

    print(player.ycor())

    if player.ycor() >= TURTLE_Y_COR_BOUNDARY:
        player.reset_player()


screen.exitonclick()
