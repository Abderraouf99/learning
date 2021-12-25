from turtle import Turtle
import time


class Snake:
    segments = []

    def __init__(self, size):
        for _ in range(size):
            self.init_segment()
        self.head = self.segments[0]

    def init_segment(self):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.pensize(20)
        segment.penup()
        position = (0, 0)
        if len(self.segments) > 0:
            position = (
                self.segments[len(self.segments) - 1].pos()[0] - 20, self.segments[len(self.segments) - 1].pos()[1])
        segment.goto(position)
        self.segments.append(segment)

    def move(self):
        time.sleep(0.1)
        for segment_index in range(len(self.segments) - 1, 0, -1):
            segment = self.segments[segment_index]
            next_segment = self.segments[segment_index - 1]
            new_x = next_segment.xcor()
            new_y = next_segment.ycor()
            segment.goto(new_x, new_y)
        head = self.segments[0]
        head.forward(20)
        return head.pos()

    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def turn_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def on_eat(self):
        tail = self.segments[len(self.segments) - 1]
        tail_heading = tail.heading()
        segment = Turtle(shape="square")
        segment.color("white")
        segment.pensize(20)
        segment.penup()
        if tail_heading == 0:
            x_position = tail.pos()[0] - 20
            y_position = tail.pos()[1]
            segment.goto(x_position, y_position)
        elif tail_heading == 180:
            x_position = tail.pos()[0] + 20
            y_position = tail.pos()[1]
            segment.goto(x_position, y_position)
        elif tail_heading == 90:
            x_position = tail.pos()[0]
            y_position = tail.pos()[1] - 20
            segment.goto(x_position, y_position)
        else:
            x_position = tail.pos()[0]
            y_position = tail.pos()[1] + 20
            segment.goto(x_position, y_position)
        self.segments.append(segment)

    def snake_ate_itself(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 5:
                return True
        return False


    def on_lose(self):
        for segment in self.segments:
            segment.color("red")