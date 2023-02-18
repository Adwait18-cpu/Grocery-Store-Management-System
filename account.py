from tkinter import *
import my_database

window = Tk()
window.title("General Store Account Management")


def display_command():
    """ Function that calls display function from database file """
    ab.delete(0, END)
    for row in my_database.display():
        ab.insert(END, row)


def search_command():
    """ Function that calls search function from database file """
    ab.delete(0, END)
    for row in my_database.search(name=name.get(), phone_number=phone_number.get()):
        ab.insert(END, row)
    display_command()


def add_command():
    """ Function that calls add function from database file """
    my_database.add(name.get(), phone_number.get(), address.get(), purchase.get(), credit.get(), cdate.get())
    ab.delete(0, END)
    ab.insert(END, name.get(), phone_number.get(), address.get(), purchase.get(), credit.get(), cdate.get())


def get_selected_row(event):
    """ This function allows to select all the parameters of a selected row """
    try:
        global selected_tuple
        index = ab.curselection()[0]
        selected_tuple = ab.get(index)
        a1.delete(0, END)
        a1.insert(END, selected_tuple[1])
        a2.delete(0, END)
        a2.insert(END, selected_tuple[2])
        a3.delete(0, END)
        a3.insert(END, selected_tuple[3])
        a4.delete(0, END)
        a4.insert(END, selected_tuple[4])
        a5.delete(0, END)
        a5.insert(END, selected_tuple[5])
        a6.delete(0, END)
        a6.insert(END, selected_tuple[6])
    except IndexError:
        pass


def update_command():
    """ Function that calls update function from database file """
    my_database.update(selected_tuple[0], name.get(), phone_number.get(), address.get(), purchase.get(), credit.get(),
                       cdate.get())
    display_command()


def delete_command():
    """ Function that calls delete function from database file """
    my_database.delete(selected_tuple[0])
    display_command()


def clear_command():
    """ Function that clears the screen """
    ab.delete(0, END)
    a1.delete(0, END)
    a2.delete(0, END)
    a3.delete(0, END)
    a4.delete(0, END)
    a5.delete(0, END)
    a6.delete(0, END)


l1 = Label(window, text="Name")
l1.grid(row=0, column=0, columnspan=3)
l2 = Label(window, text="Phone No.")
l2.grid(row=1, column=0, columnspan=3)
l3 = Label(window, text="Address")
l3.grid(row=2, column=0, columnspan=3)
l4 = Label(window, text="Purchase")
l4.grid(row=3, column=0, columnspan=3)
l5 = Label(window, text="Credit")
l5.grid(row=4, column=0, columnspan=3)
l6 = Label(window, text="Date")
l6.grid(row=5, column=0, columnspan=3)

name = StringVar()
a1 = Entry(window, textvariable=name, width=95)
a1.grid(row=0, column=0, columnspan=20)

phone_number = StringVar()
a2 = Entry(window, textvariable=phone_number, width=95)
a2.grid(row=1, column=0, columnspan=20)

address = StringVar()
a3 = Entry(window, textvariable=address, width=95)
a3.grid(row=2, column=0, columnspan=20)

purchase = StringVar()
a4 = Entry(window, textvariable=purchase, width=95)
a4.grid(row=3, column=0, columnspan=20)

credit = StringVar()
a5 = Entry(window, textvariable=credit, width=95)
a5.grid(row=4, column=0, columnspan=20)

cdate = StringVar()
a6 = Entry(window, textvariable=cdate, width=95)
a6.grid(row=5, column=0, columnspan=20)

b1 = Button(window, text="Add", width=29, command=add_command)
b1.grid(row=6, column=0)

b2 = Button(window, text="Update", width=29, command=update_command)
b2.grid(row=6, column=1)

b3 = Button(window, text="Search", width=29, command=search_command)
b3.grid(row=6, column=2)

b4 = Button(window, text="View All", width=29, command=display_command)
b4.grid(row=6, column=3)

b5 = Button(window, text="Delete", width=29, command=delete_command)
b5.grid(row=6, column=4)

b6 = Button(window, text="Exit", width=29, command=window.destroy)
b6.grid(row=6, column=5)

b7 = Button(window, text="Clear All", width=29, command=clear_command)
b7.grid(row=0, column=5)

ab = Listbox(window, height=40, width=203)
ab.grid(row=7, column=0, columnspan=6)

sb = Scrollbar(window)
sb.grid(row=7, column=6, rowspan=6)

ab.configure(yscrollcommand=sb.set)
sb.configure(command=ab.yview)

ab.bind('<<ListboxSelect>>', get_selected_row)
window.mainloop()
