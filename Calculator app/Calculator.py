from tkinter import *


def calculate():
    try:
        result = eval(screen.get())
        screen.delete(0, "end")
        screen.insert(0, result)
    except Exception as e:
        screen.delete(0, "end")
        screen.insert(0, "Error")


def clear():
    screen.delete(0, "end")


root = Tk()

root.maxsize(250, 200)
root.minsize(250, 200)

root.configure(background="orange")

root.title("Calculator")

frame = Frame(root, bg="orange")
frame.pack(pady=4)
frame1 = Frame(root, bg="brown")
frame1.pack()

heading = Label(frame, text="My Calculator", fg="white", bg="orange", font="Times 14 underline bold italic", pady=5)
heading.pack()

screen_value = StringVar()
screen_value.set("")
screen = Entry(frame, textvariable=screen_value)
screen.pack()

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("4", 1, 3),
    ("5", 2, 0), ("6", 2, 1), ("1", 2, 2), ("2", 2, 3),
    ("3", 3, 0), ("0", 3, 1), ("*", 3, 2), ("=", 3, 3),
    ("+", 4, 0), ("-", 4, 1), ("/", 4, 2), ("X", 4, 3)

]

for button in buttons:
    text, row, column = button
    if text == "=":
        Button(frame1, text=text, command=calculate, padx=5.5, bg="light green").grid(row=row, column=column, pady=1,
                                                                                      padx=1)
    elif text == "X":
        Button(frame1, text=text, command=clear, padx=6.2, bg="light green").grid(row=row, column=column, pady=1,
                                                                                  padx=1)
    else:
        Button(frame1, text=text, command=lambda text=text: screen.insert("end", text), padx=7, bg="light green").grid(
            row=row, column=column, pady=1, padx=1)

root.mainloop()
