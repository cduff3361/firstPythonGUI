from tkinter import *
from tkinter import ttk
import csv
from profile import Profile
from expense import *


master = Tk()
master.title("Personal Finance Tracker")
master.geometry("500x280")
mainProfile = Profile()


tabControl = ttk.Notebook(master)
userInfo_t = ttk.Frame(tabControl)
monExp_t = ttk.Frame(tabControl)
tabControl.add(userInfo_t, text='User Info')
tabControl.add(monExp_t, text='Monthly Expenses')
monthlyExpenseList = ExpenseList(monExp_t, master)

tabControl.pack(expand=1, fill="both")
userInfo_t.rowconfigure(0, minsize = 20)
userInfo_t.rowconfigure(4, minsize = 20)
userInfo_t.rowconfigure(6, minsize = 20)
userInfo_t.rowconfigure(7, minsize = 20)
userInfo_t.rowconfigure(8, minsize = 20)

Label(userInfo_t, text='First Name:').grid(row=1)
Label(userInfo_t, text='Last Name:').grid(row=3)
Label(userInfo_t, text='Middle Name:').grid(row=2)
Label(userInfo_t, text='Monthly Budget: $').grid(row=5, column=0)

Label(monExp_t, text = 'Monthly Expense', width = 20, bg = 'yellow').grid(row=0, column=0)
Label(monExp_t, text = 'Amount Due ($)', width = 20, bg = 'yellow').grid(row=0,column=1)
Label(monExp_t, text = 'Day of Month Due', width = 20, bg = 'yellow').grid(row=0,column=2)
Label(monExp_t, text = 'Yearly Cost ($)', width = 20, bg = 'yellow').grid(row=0,column=3)





def saveProfile(save_first, save_middle, save_last, save_monbud):

    mainProfile.changeFirstName(save_first)
    mainProfile.changeMiddleName(save_middle)
    mainProfile.changeLastName(save_last)
    mainProfile.changeMonBud(int(save_monbud))    

    OutputFirst.configure(text = save_first)
    OutputMiddle.configure(text = save_middle)
    OutputLast.configure(text = save_last)
    OutputMonBud.configure(text = save_monbud)


def clearInput():
    first.delete(0, END)
    middle.delete(0, END)
    last.delete(0, END)
    mon_budget.delete(0, END)
    #OutputFirst.delete(1.0,END)



#ms = Message(master, text=e1val)
#ms.grid(row=0, column=2)

#print(e1.get())

#OutputFirst = ourMessage = 'This is our Message'
OutputFirst = Message(userInfo_t,width=100, text='')
OutputFirst.grid(row = 1, column = 1)
OutputMiddle = Message(userInfo_t,width=100, text='')
OutputMiddle.grid(row = 2, column = 1)
OutputLast = Message(userInfo_t,width=100, text='')
OutputLast.grid(row = 3, column = 1)
OutputMonBud = Message(userInfo_t,width=100, text='')
OutputMonBud.grid(row = 5, column = 1)

'''Display = Button(userInfo_t, height = 1,
                 width = 10, 
                 text ="Save",
                 command = lambda:saveInput())
Display.grid(row=9,column=2)'''
ClearButton = Button(userInfo_t, height = 1,
                 width = 10, 
                 text ="Clear All",
                 command = lambda:clearInput())
ClearButton.grid(row=10,column=2)


def editProfile():
    editWin = Toplevel(master)
    editWin.title("Edit Profile")
    editWin.geometry("450x250")
    Label(editWin, text='First Name').grid(row=1)
    Label(editWin, text='Last Name').grid(row=3)
    Label(editWin, text='Middle Name').grid(row=2)
    Label(editWin, text='Monthly Budget: $').grid(row=5, column=0)
    firstEdit = Entry(editWin)
    middleEdit = Entry(editWin)
    lastEdit = Entry(editWin)
    mon_budget_Edit = Entry(editWin)
    firstEdit.grid(row=1, column=1)
    middleEdit.grid(row=2, column=1)
    lastEdit.grid(row=3, column=1)
    mon_budget_Edit.grid(row=5, column=1)
    firstEdit.insert(0, mainProfile.getFirstName())
    middleEdit.insert(0, mainProfile.getMiddleName())
    lastEdit.insert(0, mainProfile.getLastName())
    mon_budget_Edit.insert(0, mainProfile.getMonBud()) 
    Display = Button(editWin, height = 1,
                 width = 10, 
                 text ="Save",
                 command = lambda:saveProfile(firstEdit.get(), middleEdit.get(), lastEdit.get(), mon_budget_Edit.get()))
    Display.grid(row=9,column=2)

EditButton = Button(userInfo_t, height = 1,
                 width = 10, 
                 text ="Edit Profile",
                 command = lambda:editProfile())
EditButton.grid(row=9,column=1)


def loadProfile():
    with open('profiles1.csv', 'r') as file:
        reader = csv.reader(file, delimiter=',')
        row0 = next(reader)
        row1 = next(reader)

        OutputFirst.configure(text = mainProfile.getFirstName())
        OutputMiddle.configure(text = mainProfile.getMiddleName())
        OutputLast.configure(text = mainProfile.getLastName())
        OutputMonBud.configure(text = mainProfile.getMonBud()) 
    monthlyExpenseList.loadMonthlyExpense()
    #print(monthlyExpenseList.expenseList[0].expense + ',' + monthlyExpenseList.expenseList[0].amount)


menu = Menu(master)
master.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Load Profile',command=lambda:loadProfile())
filemenu.add_separator()
filemenu.add_command(label='Exit', command=master.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)

#monthlyExpenseList.loadMonthlyExpense()
#monthlyExpenseList.addMonthlyExpense("Rent", 1100, 1)
#monthlyExpenseList.saveMonthlyExpenses()



mainloop()


