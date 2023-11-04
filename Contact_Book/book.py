from tkinter import *
from tkinter import messagebox as mes
root = Tk()
root.configure(background="blue")
root.geometry("470x250")
root.title("Contact Book")
c = []
frame = Frame(root)
frame.pack(side=RIGHT)
Label(frame,text="My Contact Book", bg="light green", font="Times 15 bold underline").pack(fill=X)
scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Times new roman', 16), bg="#f0fffc", width=20, height=20,
                 borderwidth=3, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)


def selected():
    print("hello", len(select.curselection()))
    if len(select.curselection()) == 0:
        mes.showerror("Error", "Please Select the Name")
    else:
        return int(select.curselection()[0])


def add():
    if Name_val.get() != "" and Phone_val.get() != "" and Email_val.get() != "" and Address_val.get() != "":
        c.append([Name_val.get(), Phone_val.get(), Email_val.get(), Address_val.get()])
        print(f"{Name_val.get(), Phone_val.get(), Email_val.get(), Address_val.get()}\n")
        with open("record1.txt", "a") as f:
            f.write(f"{Name_val.get(), Phone_val.get(), Email_val.get(), Address_val.get()}\n")
        select_set()
        entry_reset()
        mes.showinfo("Success Message", "Successfully Add New Contact")
    else:
        mes.showerror("Error", "Please Fill all Entries")


def edit():
    if Name_val.get() and Email_val.get() and Address_val.get():
        c[selected()] = [Name_val.get(), Phone_val.get(), Email_val.get(), Address_val.get()]
        mes.showinfo("Confirmation", "Successfully Update Contact")
        entry_reset()
        select_set()

    elif not (Name_val.get()) and not (Email_val.get()) and not (Address_val.get()):
        mes.showerror("Error", "Please fill the information")

    else:
        if len(Name_val.get()) == "":
            mes.showerror("Error", "Please Select the Name and \n press Load button")
        else:
            message1 = """To Load the all information of \n selected row press Load button\n. """
            mes.showerror("Error", message1)


def entry_reset():
    Name_val.set('')
    Phone_val.set('')
    Email_val.set('')
    Address_val.set('')


def delete():
    if len(select.curselection()) != 0:
        result = mes.askyesno('Confirmation', 'You Want to Delete Contact\n Which you selected')
        if result:
            del c[selected()]
            select_set()
    else:
        mes.showerror("Error", 'Please select the Contact')


def view():
    NAME, PHONE, EMAIL, ADDRESS = c[selected()]
    Name_val.set(NAME)
    Phone_val.set(PHONE)
    Email_val.set(EMAIL)
    Address_val.set(ADDRESS)


def exits():
    root.destroy()


def select_set():
    c.sort()
    select.delete(0, END)
    for Name_val, Phone_val, Email_val, Address_val in c:
        select.insert(END, Name_val)


select_set()

Label(root, text="Add Contacts In Book", bg="light green", font="Times 15 bold underline").pack(fill=X)
Name_val = StringVar()
Phone_val = IntVar()
Phone_val.set("")
Email_val = StringVar()
Address_val = StringVar()
name = Label(root, text="NAME :", bg="light green", font="Times 9 bold underline")
name.place(x=10, y=40)
name_entry = Entry(root, textvariable=Name_val)
name_entry.place(x=65, y=40)
phone = Label(root, text="Phone No. :", bg="light green", font="Times 9 bold underline")
phone.place(x=10, y=70)
phone_entry = Entry(root, textvariable=Phone_val)
phone_entry.place(x=85, y=70)
email = Label(root, text="E-MAIL :", bg="light green", font="Times 9 bold underline")
email.place(x=10, y=100)
email_entry = Entry(root, textvariable=Email_val)
email_entry.place(x=72, y=100)
address = Label(root, text="ADDRESS :", bg="light green", font="Times 9 bold underline")
address.place(x=10, y=130)
address_entry = Entry(root, textvariable=Address_val)
address_entry.place(x=87, y=130)
Add_but = Button(root, text="ADD", command=add)
Add_but.place(x=40, y=160)
Edit_but = Button(root, text="EDIT", command=edit)
Edit_but.place(x=130, y=160)
Delete_but = Button(root, text="DELETE", command=delete)
Delete_but.place(x=80, y=190)
View_but = Button(root, text="VIEW", command=view)
View_but.place(x=40, y=220)
Exit_but = Button(root, text="EXIT", command=exits)
Exit_but.place(x=130, y=220)
root.mainloop()
