from turtle import Turtle
from constants import (
    TURTLE_WIDTH_FACTOR, TURTLE_HEIGHT_FACTOR,
    TURTLE_COLOR, TURTLE_SHAPE,
    TURTLE_HEADING, TURTLE_STARTING_POSITION,
    TURTLE_MOVING_DISTANCE
)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(TURTLE_SHAPE)
        self.penup()
        self.shapesize(stretch_wid=TURTLE_WIDTH_FACTOR, stretch_len=TURTLE_HEIGHT_FACTOR)
        self.color(TURTLE_COLOR)
        self.setheading(TURTLE_HEADING)
        self.reset_player()

    def move(self):
        self.sety(self.ycor() + TURTLE_MOVING_DISTANCE)

    def reset_player(self):
        self.goto(TURTLE_STARTING_POSITION)

