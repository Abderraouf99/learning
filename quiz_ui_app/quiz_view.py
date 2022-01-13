import time
import tkinter

BG_COLOR = "#406882"


class QuizView(tkinter.Tk):
    def __init__(self, initial_question):
        super().__init__()
        self.current_question = initial_question
        self.title("Quizzler")
        self.config(bg=BG_COLOR, padx=20, pady=20)
        score_label = tkinter.Label(text="score: 0", bg=BG_COLOR)
        score_label.grid(row=1, column=2)

        self.canvas = tkinter.Canvas()
        self.canvas.config(bg="white", highlightthickness=0, width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text=self.current_question["question"],
                                                     fill=BG_COLOR,
                                                     font=("Arial", 20, "italic"))

        self.canvas.grid(row=2, column=1, columnspan=2, pady=50)

        self.true_button = tkinter.Label(text="✓", bg="#2FDD92", fg="#ffffff", font=("Arial", 25, "bold"), padx=20,
                                         pady=20)
        self.true_button.bind('<Button-1>', lambda e: self.on_true_click())
        self.true_button.grid(row=3, column=1, )

        self.false_button = tkinter.Label(text="⤫", bg="#FF1700", fg="#ffffff", font=("Arial", 25, "bold"), padx=20,
                                          pady=20)
        self.false_button.grid(row=3, column=2)
        self.false_button.bind('<Button-1>', lambda y: self.on_false_click())

        tkinter.mainloop()

    def on_true_click(self):
        if self.current_question["correct_answer"] == "True":
            self.canvas.configure(bg="green")
            time.sleep(5)
            self.canvas.configure(bg="white")
            self.canvas.itemconfig(self.question_text, text="Wesh les hommes")

    def on_false_click(self):
        self.canvas.itemconfig(self.question_text, text="Wesh les hommes")
        time.sleep(2)
        self.canvas.itemconfig(self.question_text, text="Hello world")
