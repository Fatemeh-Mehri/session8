from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from tkinter import StringVar

from file_manager import *
from validator import *

account_list = read_from_file("account.dat")


def load_data(account_list):
    account_list = read_from_file("account.dat")
    for row in table.get_children():
        table.delete(row)

    for account in account_list:
        table.insert("", END, values=account)


def reset_form():
    id.set(len(account_list) + 1)
    name.set(" ")
    family.set(" ")
    amount.set(0)
    account_type.set(" ")
    creation_date.set(" ")
    status.set(" ")

    load_data(account_list)




def save_btn_click():
        account = (
        id.get(), name.get(), family.get(), amount.get(), account_type.get(), creation_date.get(),status.get())
        errors = account_validator(account)
        if amount.get() > 0:
            tag = "bestankar"
        elif amount.get() < 0:
            tag = "bedehkar"
        else:
            tag = "bihesab"
        table.insert("", END, values=account, tags=tag)
        msg.showinfo("Saved", "account saved")
        reset_form()
        if errors:
           msg.showerror("Errors", "\n".join(errors))
        else:

           account_list.append(account)
           write_to_file("account.dat", account_list)
           reset_form()


def table_select(x):
    selected_account = table.item(table.focus())["values"]
    if selected_account:
        id.set(selected_account[0])
        name.set(selected_account[1])
        family.set(selected_account[2])
        amount.set(selected_account[3])
        account_type.set(selected_account[4])
        creation_date.set(selected_account[5])
        status.set(selected_account[6])



window = Tk()
window.title("Account Info")
window.geometry("1010x470")

# Id
Label(window, text="Id").place(x=20, y=20)
id = IntVar(value=101)
Entry(window, textvariable=id, state="readonly").place(x=130, y=20)

# Name
Label(window, text="Name").place(x=20, y=60)
name = StringVar()
Entry(window, textvariable=name).place(x=130, y=60)

# Family
Label(window, text="Family").place(x=20, y=100)
family = StringVar()
Entry(window, textvariable=family).place(x=130, y=100)

# Amount
Label(window, text="Amount").place(x=20, y=140)
amount = IntVar()
Entry(window, textvariable=amount).place(x=130, y=140)


# Account_Type
Label(window, text="Account_type").place(x=20, y=180)
account_type = StringVar()
Entry(window, textvariable=account_type).place(x=130, y=180)


# Creation_Date

Label(window, text="Creation_Date").place(x=20, y=220)
creation_date = IntVar()
Entry(window, textvariable=creation_date).place(x=130, y=220)



# Status

Label(window, text="Status").place(x=20, y=260)
status = StringVar()
Entry(window, textvariable=status).place(x=130, y=260)


table = ttk.Treeview(window, columns=[1, 2, 3, 4,5,6,7], show="headings")
table.heading(1, text="Id")
table.heading(2, text="Name")
table.heading(3, text="Family")
table.heading(4, text="Amount")
table.heading(5, text="Account_Type")
table.heading(6, text="Creation_Date")
table.heading(7, text="Status")



table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)
table.column(5, width=120)
table.column(6, width=120)
table.column(7, width=100)

table.tag_configure("bestankar", background="lightgreen")
table.tag_configure("bedehkar", background="pink")
table.tag_configure("bihesab", background="yellow")



table.bind("<<TreeviewSelect>>", table_select)

table.place(x=280, y=20)

Button(window, text="Save", width=6, command=save_btn_click).place(x=80, y=350, width=80)

Button(window, text="Clear", width=6, command=reset_form).place(x=170, y=350,width=80)

reset_form()

window.mainloop()
