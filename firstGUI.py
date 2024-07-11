from tkinter import *
from tkinter import ttk
import csv



master = Tk()
master.title("Personal Finance Tracker")
master.geometry("500x280")


tabControl = ttk.Notebook(master)
userInfo_t = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(userInfo_t, text='User Info')
tabControl.add(tab2, text='Monthly Expensese')

tabControl.pack(expand=1, fill="both")
userInfo_t.rowconfigure(0, minsize = 20)
userInfo_t.rowconfigure(4, minsize = 20)
userInfo_t.rowconfigure(6, minsize = 20)
userInfo_t.rowconfigure(7, minsize = 20)
userInfo_t.rowconfigure(8, minsize = 20)

Label(userInfo_t, text='First Name').grid(row=1)
Label(userInfo_t, text='Last Name').grid(row=3)
Label(userInfo_t, text='Middle Name').grid(row=2)
Label(userInfo_t, text='Monthly Budget: $').grid(row=5, column=0)
first = Entry(userInfo_t)
middle = Entry(userInfo_t)
last = Entry(userInfo_t)
mon_budget = Entry(userInfo_t)
first.grid(row=1, column=1)
middle.grid(row=2, column=1)
last.grid(row=3, column=1)
mon_budget.grid(row=5, column=1)




def saveInput():
    firstval = first.get()
    middleval = middle.get()
    lastval = last.get()
    monthlyBudget = mon_budget.get()
    OutputFirst.delete(1.0,END)
    OutputMiddle.delete(1.0,END)
    OutputLast.delete(1.0,END)
    OutputMonBud.delete(1.0,END)
    OutputFirst.insert(END, firstval)
    OutputMiddle.insert(END, middleval)
    OutputLast.insert(END, lastval)
    OutputMonBud.insert(END, monthlyBudget)
    with open('profiles1.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["FIRST", "MIDDLE", "LAST","MONTHLY BUDGET"]
        
        writer.writerow(field)
        writer.writerow([firstval, middleval, lastval, monthlyBudget])

def clearInput():
    first.delete(0, END)
    middle.delete(0, END)
    last.delete(0, END)
    mon_budget.delete(0, END)
    #OutputFirst.delete(1.0,END)



#ms = Message(master, text=e1val)
#ms.grid(row=0, column=2)

#print(e1.get())

OutputFirst = Text(userInfo_t, height = 1, 
          width = 20, 
          bg = "light cyan")
OutputFirst.grid(row = 1, column = 2)
OutputMiddle = Text(userInfo_t, height = 1, 
          width = 20, 
          bg = "light cyan")
OutputMiddle.grid(row = 2, column = 2)
OutputLast = Text(userInfo_t, height = 1, 
          width = 20, 
          bg = "light cyan")
OutputLast.grid(row = 3, column = 2)
OutputMonBud = Text(userInfo_t, height = 1, 
          width = 20, 
          bg = "light cyan")
OutputMonBud.grid(row = 5, column = 2)

Display = Button(userInfo_t, height = 1,
                 width = 10, 
                 text ="Save",
                 command = lambda:saveInput())
Display.grid(row=9,column=2)
ClearButton = Button(userInfo_t, height = 1,
                 width = 10, 
                 text ="Clear All",
                 command = lambda:clearInput())
ClearButton.grid(row=10,column=2)


def loadProfile():
    with open('profiles1.csv', 'r') as file:
        reader = csv.reader(file, delimiter=',')
        row0 = next(reader)
        row1 = next(reader)

        OutputFirst.delete(1.0,END)
        OutputMiddle.delete(1.0,END)
        OutputLast.delete(1.0,END)
        OutputMonBud.delete(1.0,END)
        OutputFirst.insert(END, row1[0])
        OutputMiddle.insert(END, row1[1])
        OutputLast.insert(END, row1[2])
        OutputMonBud.insert(END, row1[3])            


menu = Menu(master)
master.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...',command=lambda:loadProfile())
filemenu.add_separator()
filemenu.add_command(label='Exit', command=master.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)



mainloop()


