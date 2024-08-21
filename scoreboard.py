from turtle import Turtle
from constants import (
    SCORE_BOARD_POSITION, SCOREBOARD_ALIGNMENT, SCOREBOARD_FONT, SCOREBOARD_COLOR
)


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color(SCOREBOARD_COLOR)
        self.hideturtle()
        self.penup()
        self.goto(SCORE_BOARD_POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Level: {self.level}", move=False, align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", move=False, align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()
