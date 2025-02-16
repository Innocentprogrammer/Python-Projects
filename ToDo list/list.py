# Here import all thing including messagebox from the TKINTER library of PYTHON
from tkinter import *
from tkinter import messagebox as mes

# This set of code is used to give the title of the TKINTER APP, Set the Dimension of APP, and Set the Background color.
root = Tk()
root.title("TO DO List App")
root.minsize(500, 400)
root.maxsize(550, 550)
root.configure(bg="Pink")

# This set of code is used to generate a listbox
frame = Frame(root)
frame.pack()
Label(frame, text="TO DO List", bg="Yellow", font="Times 15 bold underline").pack(fill=X)
scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Times new roman', 16), bg="#f0fffc", width=50, height=10,
                 borderwidth=3, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)

# This is an empty list to insert the task list into it
c = []


# This function add the task into listbox
def add():
    if TaskEntry.get() != "":
        c.append(TaskEntry.get())
        select_set()
        entry_reset()
        mes.showinfo("Success Message", "New Task Edit Successfully")
    else:
        mes.showerror("Error", "Please Fill all Entries")


# This function clear the entry widget
def entry_reset():
    TaskValue.set('')


# This function show the added task into listbox
def select_set():
    select.delete(0, END)
    for i in c:
        select.insert(END, i)


# Selected function to select the task from list box
def selected():
    if len(select.curselection()) == 0:
        mes.showerror("Error", "Please Select the Name")
    else:
        return int(select.curselection()[0])


# Delete function to delete the completed task from the list
def delete():
    if len(select.curselection()) != 0:
        result = mes.askyesno('Confirmation', 'Do you want to Delete the selected task? ')
        if result:
            del c[selected()]
            select_set()
            mes.showinfo("Success Message", "Task Deleted Successfully")
    elif len(c) == 0:
        mes.showerror("Error", 'Task list is empty')
    else:
        mes.showerror("Error", 'Please select the Task')


# Message in the form of label
Task = Label(root, text="Enter Your Task", bg="light green", font="Times 15 bold underline")
Task.pack(pady=5, fill=X)

# Entry Widget to Get the task from the user
TaskValue = StringVar()
TaskEntry = Entry(root, textvariable=TaskValue, width=100, font=("Times New Roman", 15, "bold"))
TaskEntry.pack(ipadx=2, ipady=2)

# Button Frame to show both button on same line
button_frame = Frame(root, bg="Light Blue")
button_frame.pack(pady=5)

# Add task Button
add_button = Button(button_frame, text="Add Task", command=add)
add_button.pack(side=LEFT, padx=10)

# Delete Task Button
delete_button = Button(button_frame, text="Delete Task", command=delete)
delete_button.pack(side=LEFT, padx=10)

root.mainloop()
