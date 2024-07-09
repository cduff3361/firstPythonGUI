from tkinter import *

master = Tk()
Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=2)
Label(master, text='Middle Name').grid(row=1)
first = Entry(master)
middle = Entry(master)
last = Entry(master)
first.grid(row=0, column=1)
middle.grid(row=1, column=1)
last.grid(row=2, column=1)


def saveInput():
    OutputFirst.insert(END, first.get() + ' ' + middle.get() + ' ' + last.get())


#e1val = e1.get()
#e2val = e2.get()

#ms = Message(master, text=e1val)
#ms.grid(row=0, column=2)

#print(e1.get())

OutputFirst = Text(master, height = 1, 
          width = 25, 
          bg = "light cyan")
OutputFirst.grid(row = 1, column = 3)

Display = Button(master, height = 1,
                 width = 5, 
                 text =">>",
                 command = lambda:saveInput())
Display.grid(row=1,column=2)




mainloop()