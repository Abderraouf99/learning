from turtle import Turtle


class ScoreBoard:
    def __init__(self):
        self.score_segments = []
        self.left_score = 0
        self.right_score = 0
        self.build_segments()

    def build_segments(self):
        positions = [(-30, 170), (30, 170)]
        for position in positions:
            segment = Turtle()
            segment.penup()
            segment.hideturtle()
            segment.color("white")
            segment.speed("fastest")
            segment.goto(position)
            if position[1] == -30:
                segment.write(f"{self.left_score}", move=False, align="center", font=("Arial", 24, 'normal'))
            else:
                segment.write(f"{self.right_score}", move=False, align="center", font=("Arial", 24, 'normal'))
            self.score_segments.append(segment)

    def increase_score(self, position):
        if position[0] > 350:
            self.increase_left_score()
        else:
            self.increase_right_score()


    def update_text_score(self, turtle_obj, score):
        old_position = turtle_obj.pos()
        print(old_position)
        turtle_obj.clear()
        turtle_obj.goto(old_position)
        turtle_obj.color("white")
        turtle_obj.hideturtle()
        turtle_obj.write(f"{score}", move=False, align="center", font=("Arial", 24, 'normal'))

    def increase_left_score(self):
        self.left_score += 1
        self.update_text_score(self.score_segments[0], self.left_score)

    def increase_right_score(self):
        self.right_score += 1
        self.update_text_score(self.score_segments[1], self.right_score)

