import random
from tkinter import *
from tkinter import messagebox as message
root = Tk()
root.geometry("400x300")
root.configure(background="light green")
root.title("Rock Paper Scissor Game")


def submit():
    selection()


def selection():
    s = radio.get()
    if s == 1:
        label.config(text="Your Choice is: Rock")
    elif s == 2:
        label.config(text="Your Choice is: Paper")
    else:
        label.config(text="Your Choice is: Scissor")
    l = [1, 2, 3]
    r = (random.choice(l))
    if r == 1:
        label1.config(text="Computer's Choice is: Rock")
    elif r == 2:
        label1.config(text="Computer's Choice is: Paper")
    else:
        label1.config(text="Computer's Choice is: Scissor")
    if s == r:
        label2.config(text="Draw 🤝🏻")
    elif (s == 1 and r == 3) or (s == 2 and r == 1) or (s == 3 and r == 2):
        label2.config(text="you won 👍🏻")
    elif (s == 1 and r == 2) or (s == 2 and r == 3) or (s == 3 and r == 1):
        label2.config(text="you loss 👎🏻")
    m = message.askquestion("play more", "Want to play more?")
    if m == "no":
        root.destroy()


Label(root, text="Welcome to Rock Paper Scissor Game", bg="light green", font="Times 15 bold underline").pack()
inp = Label(root, text="Enter Your Choice :", bg="light green", font="Times 12")
inp.pack()
radio = IntVar()
o1 = Radiobutton(root, text="Rock", variable=radio, value=1,  bg="light green", font="Times 12")
o1.pack()
o2 = Radiobutton(root, text="Paper", variable=radio, value=2, bg="light green", font="Times 12")
o2.pack()
o3 = Radiobutton(root, text="Scissor", variable=radio, value=3,  bg="light green", font="Times 12")
o3.pack()

frame = Frame(root)
frame.pack()
sub = Button(frame, text="Submit", command=submit)
sub.grid(row=0)
label = Label(root, bg="light green", font="Times 13")
label.pack()
label1 = Label(root, bg="light green", font="Times 13")
label1.pack()
label2 = Label(root, bg="light green", font="Times 20 bold")
label2.pack()
root.mainloop()
