from tkinter import *
from tkinter import messagebox as mes
import os
from plyer import notification

# Root configuration
root = Tk()
root.title("TO DO List App")
root.geometry("800x400")
root.resizable(0, 0)
root.configure(bg="light blue")

# Task list with priority and status
tasks = []
editing_index = -1

# Load tasks from file
def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(eval(line.strip()))
        sort_tasks()
        select_set()

# Save tasks to file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(str(task) + "\n")

# Sort tasks by priority
def sort_tasks():
    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    tasks.sort(key=lambda x: priority_order[x["priority"]])

# Add a new task
def add():
    if TaskEntry.get() != "":
        task = {"name": TaskEntry.get(), "priority": priority_var.get(), "status": "Pending"}
        tasks.append(task)
        sort_tasks()
        select_set()
        entry_reset()
        mes.showinfo("Success Message", "New Task Added Successfully")
        save_tasks()
    else:
        mes.showerror("Error", "Please fill all entries")

# Clear the entry field
def entry_reset():
    TaskValue.set('')
    priority_var.set("Medium")
    global editing_index
    editing_index = -1

# Display tasks in the listbox
def select_set():
    select.delete(0, END)
    for task in tasks:
        display_text = f"{task['name']} | Priority: {task['priority']} | Status: {task['status']}"
        select.insert(END, display_text)

# Get the selected task
def selected():
    if len(select.curselection()) == 0:
        mes.showerror("Error", "Please select a task")
    else:
        return int(select.curselection()[0])

# Delete the selected task
def delete():
    if len(select.curselection()) != 0:
        result = mes.askyesno('Confirmation', 'Do you want to delete the selected task?')
        if result:
            del tasks[selected()]
            sort_tasks()
            select_set()
            mes.showinfo("Success Message", "Task Deleted Successfully")
            save_tasks()
    elif len(tasks) == 0:
        mes.showerror("Error", 'Task list is empty')
    else:
        mes.showerror("Error", 'Please select a task')

# Edit the selected task
def edit():
    global editing_index
    if len(select.curselection()) == 0:
        mes.showerror("Error", "Please select a task to edit")
    else:
        editing_index = selected()
        task = tasks[editing_index]
        TaskValue.set(task['name'])
        priority_var.set(task['priority'])

# Update the task after editing
def update():
    global editing_index
    if editing_index == -1:
        mes.showerror("Error", "No task is being edited")
    elif TaskEntry.get() == "":
        mes.showerror("Error", "Please fill all entries")
    else:
        tasks[editing_index] = {"name": TaskEntry.get(), "priority": priority_var.get(), "status": "Pending"}
        sort_tasks()
        select_set()
        entry_reset()
        mes.showinfo("Success Message", "Task Updated Successfully")
        save_tasks()

# Mark the selected task as done
def mark_done():
    if len(select.curselection()) == 0:
        mes.showerror("Error", "Please select a task")
    else:
        index = selected()
        tasks[index]["status"] = "Completed"
        sort_tasks()
        select_set()
        save_tasks()

# Send notifications based on the user's selected interval
def send_reminder():
    pending_tasks = [task for task in tasks if task["status"] == "Pending"]
    incomplete_tasks = [task["name"] for task in tasks if task["status"] == "Pending"]
    if pending_tasks:
        notification.notify(
            title="Task Reminder",
            message=f"You have {len(incomplete_tasks)} incomplete task(s):\n" + "\n".join(incomplete_tasks),
            timeout=5
        )
    interval = int(interval_var.get()) * 60000
    root.after(interval, send_reminder)

# UI Components
Label(root, text="TO DO List", bg="light blue", font="Times 15 bold underline").pack()

# Task input fields
frame_input = Frame(root, bg="light blue")
frame_input.pack()

TaskLabel = Label(frame_input, text="Enter Your Task:", bg="light blue", font="Times 12 bold")
TaskLabel.grid(row=0, column=0, padx=10, sticky="w")
TaskValue = StringVar()
TaskEntry = Entry(frame_input, textvariable=TaskValue, width=60, font=("Times New Roman", 14, "bold"))
TaskEntry.grid(row=0, column=1, padx=10, pady=5)

# Buttons below the task input
button_frame = Frame(root, bg="light blue")
button_frame.pack()

add_button = Button(button_frame, text="Add Task", command=add, width=15)
add_button.pack(side=LEFT, padx=10)
delete_button = Button(button_frame, text="Delete Task", command=delete, width=15)
delete_button.pack(side=LEFT, padx=10)
edit_button = Button(button_frame, text="Edit Task", command=edit, width=15)
edit_button.pack(side=LEFT, padx=10)
update_button = Button(button_frame, text="Update Task", command=update, width=15)
update_button.pack(side=LEFT, padx=10)
mark_done_button = Button(button_frame, text="Mark as Done", command=mark_done, width=15)
mark_done_button.pack(side=LEFT, padx=10)

# Priority and Notification Interval Frame
priority_interval_frame = Frame(root, bg="light blue")
priority_interval_frame.pack(pady=10)

priority_label = Label(priority_interval_frame, text="Select Priority:", bg="light blue", font="Times 12 bold")
priority_label.grid(row=0, column=0, padx=10, sticky="w")
priority_var = StringVar(value="High")
priority_menu = OptionMenu(priority_interval_frame, priority_var, "High", "Medium", "Low")
priority_menu.grid(row=0, column=1, padx=10, sticky="w")

interval_label = Label(priority_interval_frame, text="Set Notification Interval (minutes):", bg="light blue", font="Times 12 bold")
interval_label.grid(row=0, column=2, padx=10, sticky="w")
interval_var = StringVar(value="2")
interval_entry = Entry(priority_interval_frame, textvariable=interval_var, width=10, font=("Times New Roman", 14, "bold"))
interval_entry.grid(row=0, column=3, padx=10, sticky="w")

# Task listbox
frame = Frame(root, bg="light blue")
frame.pack()

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Times new roman', 14), bg="#f0fffc", width=80, height=10,
                 borderwidth=3, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)

# Load tasks at startup
load_tasks()

# Start reminder notifications
send_reminder()

# Run the application
root.mainloop()
