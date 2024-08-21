from turtle import Turtle
import random
from constants import (
    CAR_WIDTH_FACTOR, CAR_HEIGHT_FACTOR,
    CAR_COLORS, CAR_SHAPE,
    CAR_HEADING, CAR_X_STARTING_POSITION,
    CAR_UPPER_Y_LIMIT, CAR_LOWER_Y_LIMIT,
    CAR_WIDTH,
    CAR_STARTING_MOVE_SPEED, CAR_MOVE_SPEED_INCREMENT
)


class Car(Turtle):
    def __init__(self, y_position):
        super().__init__()
        self.shape(CAR_SHAPE)
        self.penup()
        self.shapesize(stretch_wid=CAR_WIDTH_FACTOR, stretch_len=CAR_HEIGHT_FACTOR)
        self.color(random.choice(CAR_COLORS))
        self.setx(CAR_X_STARTING_POSITION)
        self.sety(y_position)
        self.setheading(CAR_HEADING)

    def move(self, speed):
        self.setx(self.xcor() - speed)


class CarManager:

    def __init__(self):
        self.cars = []
        self.speed = CAR_STARTING_MOVE_SPEED

    def generate_car(self):
        random_y_position = random.randint(CAR_LOWER_Y_LIMIT, CAR_UPPER_Y_LIMIT)
        print(CAR_LOWER_Y_LIMIT)
        print(CAR_UPPER_Y_LIMIT)
        new_car = Car(random_y_position)
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.move(self.speed)

    def update_speed(self):
        self.speed += CAR_MOVE_SPEED_INCREMENT

