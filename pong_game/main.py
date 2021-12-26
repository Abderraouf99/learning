from turtle import Screen, Turtle
from pong_handle import PongHandle
from ball import Ball
from score_board import ScoreBoard
screen = Screen()
dashed_separator = Turtle()
play = True


def set_up_screen():
    screen.setup(width=800, height=400)
    screen.bgcolor("black")


def init_dashed_separator():
    dashed_separator.penup()
    dashed_separator.goto(0, -200)
    dashed_separator.hideturtle()
    dashed_separator.setheading(90)
    dashed_separator.speed("fastest")
    dashed_separator.color("white")
    dashed_separator.pensize(5)


def draw_dashed_separator():
    while dashed_separator.pos()[1] <= 200:
        dashed_separator.pendown()
        dashed_separator.forward(10)
        dashed_separator.penup()
        dashed_separator.forward(10)


def on_quit():
    global play
    play = False


set_up_screen()  # setting the background of the screen to black
init_dashed_separator()  # init the dashed line
draw_dashed_separator()  # drawing the dashed line

left_pong_handle = PongHandle(init_segment_position=(-360, 0))
right_pong_handle = PongHandle(init_segment_position=(360, 0))

ball = Ball()
score_board = ScoreBoard()
screen.listen()

screen.onkey(key="Up", fun=right_pong_handle.move_up)
screen.onkey(key="Down", fun=right_pong_handle.move_down)

screen.onkey(key="w", fun=left_pong_handle.move_up)
screen.onkey(key="s", fun=left_pong_handle.move_down)

screen.onkey(key="q", fun=on_quit)
while play:
    ball.move()
    if ball.ball_collide_wall():
        ball.handle_wall_collision()
    if ball.has_scored():
        ball.center()
        score_board.increase_score(ball.pos())
    if ball.ball_collide_with_handle(left_pong_handle) or ball.ball_collide_with_handle(right_pong_handle):
        ball.on_pong_collision()

screen.exitonclick()
