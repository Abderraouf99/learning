import turtle
from turtle import Turtle, Screen
import random

turtle_red = Turtle(shape="turtle")
turtle_red.color("red")
turtle_green = Turtle(shape="turtle")
turtle_green.color("green")
turtle_blue = Turtle(shape="turtle")
turtle_blue.color("blue")
turtle_purple = Turtle(shape="turtle")
turtle_purple.color("purple")
screen = Screen()
screen.setup(width=500, height=400)
turtles_array = [turtle_red, turtle_purple, turtle_blue, turtle_green]



def init_race():
    y_position = 0
    for racing_turtle in turtles_array:
        racing_turtle.penup()
        racing_turtle.goto(-230, y_position)
        y_position += 40


max_distance = 230
winning_turtle_position = 0
winning_turtle_color = ""

def race():
    global winning_turtle_position
    global winning_turtle_color
    for racing_turtle in turtles_array:
        random_distance = random.random() * 10
        racing_turtle.forward(random_distance)
        if racing_turtle.pos()[0] > winning_turtle_position:
            winning_turtle_position = racing_turtle.pos()[0]
            winning_turtle_color = racing_turtle.pencolor()


init_race()
bet = input("Which turtle do you want to bet on ? [red, green, purple, blue] \n")
while winning_turtle_position <= max_distance:
    race()

print(winning_turtle_color + " turtle won !")
if winning_turtle_color == bet:
    print("Congrats ! \n")
else:
    print("Try again :( \n")
screen.exitonclick()
