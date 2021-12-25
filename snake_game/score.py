from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 220)
        self.color("white")
        self.hideturtle()
        self.write(f"Score = {self.score} ", align="center", font=("Arial", 12, "normal"))

    def add_score(self):
        self.clear()
        self.goto(0, 220)
        self.color("white")
        self.hideturtle()
        self.score += 1
        self.write(f"Score = {self.score} ", align="center", font=("Arial", 12, "normal"))

