from tkinter import *
import csv

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
    firstval = first.get()
    middleval = middle.get()
    lastval = last.get()
    OutputFirst.insert(END, firstval + ' ' + middleval + ' ' + lastval)
    with open('profiles1.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["FIRST", "MIDDLE", "LAST"]
        
        writer.writerow(field)
        writer.writerow([firstval, middleval, lastval])


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


