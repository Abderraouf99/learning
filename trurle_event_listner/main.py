from turtle import Turtle, Screen

drawer = Turtle()


def move_forward():
    drawer.forward(10)


def move_backward():
    drawer.backward(10)


def turn_right():
    drawer.right(10)


def turn_left():
    drawer.left(10)


def clear_canvas():
    drawer.clear()
    drawer.penup()
    drawer.goto(0, 0)
    drawer.pendown()


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear_canvas)
screen.exitonclick()
