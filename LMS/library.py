from tkinter import *
import sqlite3
from tkinter import messagebox as msg

con = sqlite3.connect("LMS.db")
cursor = con.cursor()

cursor.execute('''
create table if not exists lms(id int primary key, bookname varchar(20), authorname varchar(20), Borroworname varchar(20))
''')
con.commit()


def add():
    idb = Id_entry.get()
    bookname = B_name_enter.get()
    authorname = A_name_enter.get()
    Borroworname = Bo_name_enter.get()
    cursor.execute('insert into lms(id,bookname,authorname,Borroworname) values (?,?,?,?)', (idb, bookname, authorname, Borroworname))
    con.commit()
    clear_entries()
    msg.showinfo('Complete Entry', "Book Entry Done Successfully")
    print(f"Book information- {idb, bookname, authorname, Borroworname}. Book Add successfully")


def clear_entries():
    Id_entry.delete(0, END)
    B_name_enter.delete(0, END)
    A_name_enter.delete(0, END)
    Bo_name_enter.delete(0, END)


def m():
    root.destroy()
    import Allinone


root = Tk()
root.maxsize(400, 400)
root.minsize(200, 100)
root.title("LMS")
idval = IntVar()
Bname = StringVar()
Aname = StringVar()
Boname = StringVar()
Id = Label(root, text="Book ID : ")
Id.grid(row=0, column=0)
Id_entry = Entry(root, textvariable=Id)
Id_entry.grid(row=0, column=1)
B_name = Label(root, text="Book Name :")
B_name.grid(row=1, column=0)
B_name_enter = Entry(root, textvariable=Bname)
B_name_enter.grid(row=1, column=1)
A_name = Label(root, text="Author Name :")
A_name.grid(row=2, column=0)
A_name_enter = Entry(root, textvariable=Aname)
A_name_enter.grid(row=2, column=1)
Bo_name = Label(root, text="Borrower Name :")
Bo_name.grid(row=3, column=0)
Bo_name_enter = Entry(root, textvariable=Boname)
Bo_name_enter.grid(row=3, column=1)
add_button = Button(root, text="ADD BOOK", command=add)
add_button.grid(row=4, column=0, columnspan=2)
Button(text="Main", command=m).grid(columnspan=2)
root.mainloop()
con.close()
