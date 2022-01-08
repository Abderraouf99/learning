import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Adding label
window_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
window_label.pack()

count = 0


def on_button_click():
    global window_label, count
    count += 1
    window_label.config(text=f"Button got clicked {count} times")


# Adding a button
window_button = tkinter.Button(text="Click me !", command=on_button_click)
window_button.pack()


# Adding an entry (text field)
window_entry_text = tkinter.StringVar()
window_entry = tkinter.Entry(width=10, textvariable=window_entry_text)
window_entry.pack()

print(window_entry_text.get())
window.mainloop()
