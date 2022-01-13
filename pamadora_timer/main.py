import tkinter

PINK_COLOR = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


def on_start_counter():
    print("print")


def on_reset_counter():
    print("end")

def on_count():
    print("counting")

window = tkinter.Tk()
window.minsize(width=200, height=223)
window.config(bg=YELLOW)


window.after(1000, on_count )

image = tkinter.PhotoImage(file="tomato.png")
window.minsize(width=400, height=500)
window.config(padx=100, pady=50)
app_label = tkinter.Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
app_label.grid(row=1, column=3)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=image)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=3)

start_button = tkinter.Button(text="Start", highlightthickness=0, command=on_start_counter)
start_button.grid(row=3, column=1)

end_button = tkinter.Button(text="Reset", highlightthickness=0, command=on_reset_counter)
end_button.grid(row=3, column=4)

check_marks = tkinter.Label(text="✅", bg=YELLOW)
check_marks.grid(row=3, column=3)

window.mainloop()
