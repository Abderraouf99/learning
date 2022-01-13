import turtle
import pandas

data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()


def on_image_click(x, y):
    global data
    answer_prompt = screen.textinput(title="Guess the state", prompt="Enter the name of the state you clicked on !")
    if answer_prompt is not None:
        answer_prompt = answer_prompt.capitalize()
        if answer_prompt in all_states:
            state_data = data[data.state == answer_prompt]
            guessed_state_coord = (float(state_data.x), float(state_data.y))
            if guessed_state_coord[0] - 10 <= x <= guessed_state_coord[0] + 10 and guessed_state_coord[1] - 10 <= y <= \
                    guessed_state_coord[1] + 10:
                t = turtle.Turtle()
                t.hideturtle()
                t.penup()
                t.goto(guessed_state_coord)
                t.write(answer_prompt)
            else:
                print("You guess wrong")


screen = turtle.Screen()
screen.title("US states quiz")
image_path = "blank_states_img.gif"
screen.addshape(image_path)
turtle.shape(image_path)
screen.onscreenclick(on_image_click)

turtle.mainloop()
