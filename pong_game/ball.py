import time
from turtle import Turtle, Screen
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pensize(5)
        self.color("green")
        self.penup()
        self.goto(0, 0)
        angle = random.random() * 360
        self.setheading(angle)
        self.screen = Screen()
        self.speed("fastest")

    def move(self):
        self.forward(10)

    def ball_collide_wall(self):
        return self.ycor() >= 195 or self.ycor() <= - 195

    def handle_wall_collision(self):
        if self.ycor() >= 195:
            self.goto(self.xcor(), 182)
        else:
            self.goto(self.xcor(), -182)
        ball_heading = self.heading()
        self.setheading(-ball_heading)

    def has_scored(self):
        return self.xcor() > 380 or self.xcor() < -380

    def center(self):
        self.goto(0, 0)
        time.sleep(0.5)
        angle = random.random() * 360
        self.setheading(angle)

    def ball_collide_with_handle(self, pong):
        return (self.xcor() >= 335 or self.xcor() <= -335) and pong.get_lower_y() <= self.ycor() <= pong.get_higher_y()

    def on_pong_collision(self):
        if self.xcor() >= 335:
            self.goto(335, self.ycor())
        elif self.xcor() <= -335:
            self.goto(-335, self.ycor())
        ball_heading = self.heading()
        self.setheading(180 - ball_heading)
