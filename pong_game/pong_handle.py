from turtle import Turtle, Screen


class PongHandle(Turtle):

    def __init__(self, init_segment_position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(init_segment_position[0], init_segment_position[1])

    def move_up(self):
        if self.ycor() < 195:
            new_y = self.ycor() + 10
            self.sety(new_y)

    def move_down(self):
        if self.ycor() > - 195:
            new_y = self.ycor() - 10
            self.sety(new_y)

    def get_bouncing_surface(self):
        pong_x = self.xcor()
        pong_y = self.ycor()
        if pong_x < 0:
            pong_x += 0.5
        else:
            pong_x -= 0.5

        return [(pong_x, pong_y + 2.5), (pong_x, pong_y - 2.5)]

    def get_lower_y(self):
        return self.ycor() - 30

    def get_higher_y(self):
        return self.ycor() + 30
