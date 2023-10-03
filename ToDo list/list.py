from tkinter import *


def add_btn():
    task = task_entry.get()
    time = time_entry.get()
    lb.insert("end", f"{task} at {time}")
    task_entry.delete(0, "end")
    time_entry.delete(0, "end")


def del_btn():
    selected_task = lb.curselection()
    lb.delete(selected_task)


root = Tk()

root.title("TO DO LIST")

root.geometry("425x300")

root.maxsize(425, 300)
root.minsize(425, 300)

root.configure(background="grey")

frame = Frame(root)
frame.pack(fill=X)

frame1 = Frame(root)
frame1.pack(pady=3, fill=X)

frame2 = Frame(root)
frame2.pack(pady=2, fill=X)

heading = Label(frame, text="Welcome to TO DO LIST App", font="Times 12 underline bold italic", fg="white", bg="blue",
                pady=10, relief=RIDGE)
heading.pack(fill=X, pady=2)

t = Label(frame1, text="Enter Task:", font="Times 12 italic")
t.grid(pady=2, column=0)

task_entry = Entry(frame1)
task_entry.grid(pady=2, row=0, column=1)

t1 = Label(frame1, text="Enter Time:", font="Times 12 italic")
t1.grid(pady=2, row=0, column=2)

time_entry = Entry(frame1)
time_entry.grid(pady=2, row=0, column=3)

add_task = Button(frame1, text="Add Task", font="Times 10 italic", fg="white", bg="green", pady=3, command=add_btn)
add_task.grid(pady=2, row=1, column=1)

del_task = Button(frame1, text="Delete Task", font="Times 10 italic", fg="white", bg="red", pady=3, command=del_btn)
del_task.grid(pady=2, row=1, column=2)

tasklist = Label(frame2, text="Task List:", font="Times 12 italic")
tasklist.pack(pady=2, side=LEFT)

lb = Listbox(frame2, selectmode=SINGLE)
lb.pack(pady=2, fill=X)
root.mainloop()
