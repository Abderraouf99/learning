from turtle import Screen
from snake import Snake
from food import Food
from score import Score
screen = Screen()


def init_screen():
    screen.bgcolor("black")
    screen.title("Sneaky Snake ð")
    screen.setup(width=500, height=500)
    screen.tracer(0)


run_game = True

init_screen()
snake = Snake(size=3)
food = Food()
score = Score()
screen.listen()
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)
screen.onkey(key="Up", fun=snake.turn_up)
screen.onkey(key="Down", fun=snake.turn_down)
while run_game:
    head_position = snake.move()
    if snake.head.distance(food) < 15:
        food.on_food_eaten()
        snake.on_eat()
        score.add_score()
    if head_position[0] > 230 or head_position[0] < -230 or head_position[1] > 230 or head_position[1] < -230 or snake.snake_ate_itself():
        run_game = False
        snake.on_lose()

    screen.update()

screen.exitonclick()
