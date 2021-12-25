from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        position_x = random.randint(-230, 230)
        position_y = random.randint(-230, 230)
        self.goto(position_x, position_y)

    def on_food_eaten(self):
        position_x = random.randint(-230, 230)
        position_y = random.randint(-230, 230)
        self.goto(position_x, position_y)
