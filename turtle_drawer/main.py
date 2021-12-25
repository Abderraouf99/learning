import turtle
from turtle import Turtle, Screen
from random import random, choice
import colorgram


def get_colors_from_image(image_path):
    colors = colorgram.extract(image_path, 10)
    rgb_colors = []
    for color in colors:
        red = color.rgb.r
        green = color.rgb.g
        blue = color.rgb.b
        rgb_colors.append((red, green, blue))
    return rgb_colors


if __name__ == '__main__':
    distance = 100
    drawer = Turtle()
    # drawer.color("red")
    # drawer.forward(distance)
    # drawer.left(90)
    # drawer.forward(distance)
    # drawer.left(90)
    # drawer.forward(distance)
    # drawer.left(90)
    # drawer.forward(distance)
    #
    # ## Drawing a dashed line
    # active_length = 10
    # total_length = 200
    # current_length = 0
    # drawer.color("black")
    # while current_length < total_length:
    #     drawer.pendown()
    #     drawer.forward(active_length)
    #     current_position = drawer.pos()
    #     drawer.penup()
    #     drawer.goto(current_position[0]+5, current_position[1])
    #     current_length = current_length + active_length + 5
    #
    # # Drawing the weird shape
    # drawer.pendown()
    # number_of_sides = [3, 4, 5, 6, 7, 8, 9, 10]
    # for shape in number_of_sides:
    #     angle = 360 / shape
    #     number_of_sides_drawn = 0
    #
    #     red = random()
    #     green = random()
    #     blue = random()
    #     drawer.color(red, green, blue)
    #     while number_of_sides_drawn <= shape:
    #         drawer.forward(100)
    #         drawer.right(angle)
    #         number_of_sides_drawn += 1
    # turtle.clearscreen()
    # turtle.forward(100)
    # drawer.pensize(10)
    # number_of_steps = int(random() * 80)
    # possible_angles = [-90, 90]
    # possible_direction = ["left", "right"]
    # drawer.width = 20
    # print(number_of_steps)
    # for step in range(number_of_steps):
    #     # random color
    #     red = random()
    #     green = random()
    #     blue = random()
    #     drawer.color(red, green, blue)
    #
    #     # random angle
    #     random_angle = choice(possible_angles)
    #     random_direction = choice(possible_direction)
    #     if random_direction == "left":
    #         drawer.left(random_angle)
    #     else:
    #         drawer.right(random_angle)
    #     # random distance
    #     drawer.forward(50)

    # number_of_circles = 360

    # while number_of_circles > 0:
    #     red = random()
    #     green = random()
    #     blue = random()
    #     drawer.color(red, green, blue)
    #
    #     drawer.circle(100)
    #     number_of_circles -= 5
    #     drawer.left(5)
    drawer.speed("fastest")
    colors = get_colors_from_image("picture.png")
    screen = Screen()
    screen_width = turtle.Screen().canvwidth
    screen_height = turtle.Screen().canvheight
    turtle.penup()
    turtle.goto(-screen_width, -screen_height)
    turtle.pendown()
    turtle.clear()
    number_of_rows = int(screen_height / 20)
    number_of_columns = int(screen_width / 20)
    for row in range(number_of_rows):
        for col in range(number_of_columns):
            random_color = choice(colors)
            turtle.color(random_color[0]/255, random_color[1]/255, random_color[2]/255)
            turtle.dot(20)
            turtle.penup()
            turtle.forward(30)
            turtle.pendown()
        turtle.penup()
        turtle.goto(-screen_width, turtle.pos()[1] + 30)
        turtle.pendown()

    turtle.mainloop()




