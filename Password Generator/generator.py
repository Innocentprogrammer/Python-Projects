from tkinter import *
import string
import random


def gen():
    text = entry.get()
    l = int(length.get())
    character_list = ""

    if text == "1":
        character_list += (string.ascii_letters+string.digits)
    elif text == "2":
        character_list += (string.digits+string.punctuation)
    elif text == "3":
        character_list += (string.punctuation+string.ascii_letters)
    elif text == "4":
        character_list += (string.punctuation + string.ascii_letters+string.digits)
    else:
        password1.config(text="Invalid Input")

    password = []

    for i in range(l):
        random_char = random.choice(character_list)
        password.append(random_char)
    pas = ""
    for i in password:
        pas += i
    password1.config(text=f"Your Password is {pas}")


root = Tk()
root.geometry("300x200")
root.title("Password Generator")
root.configure(background="Light blue")

Label(root, text="Which type of Password you want to Generate:", bg="light blue").pack()
Label(root, text="1. Alphabet & Number \n2. Number & Special Character \n3. Special Character & Alphabet\n4. Alphabet, "
                 "Number & Special Character", bg="light blue", justify="left").pack()

entry_value = IntVar()
entry = Entry(root, textvariable=entry_value)
entry.pack()

Label(root, text="Enter the length:", bg="light blue").pack(pady=2)
length_value = IntVar()
length = Entry(root, textvariable=length_value)
length.pack()

Button(root, text="Generate", command=gen).pack(pady=2)

password1 = Label(root, text="", fg="green", bg="light blue", font="Times 12 bold")
password1.pack()

root.mainloop()
