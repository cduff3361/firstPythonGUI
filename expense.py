import csv 
from tkinter import ttk
from tkinter import *

'''def createSaveButtonForExpense(frame:ttk.Frame, expense:MonthlyExpense, buttonRow):
    SaveButton = Button(frame, height = 1,
                 width = 10, 
                 text ="Clear All",
                 command = lambda:expense.updateExpense())
    SaveButton.grid(row=buttonRow,column=5)'''




class MonthlyExpense:
    
    def __init__(self, expenseName, amount, monthlyDueDate, buttonIndex, frame:ttk.Frame):
        self.expense = expenseName
        self.amount = int(amount) 
        self.monDueDate = monthlyDueDate
        self.yearlyCost = int(amount) * 12
        self.editButton = Button(frame, height = 1,
                 width = 10, 
                 text ="Edit",
                 command = lambda:self.updateExpense())
        self.editButton.grid(row = buttonIndex, column = 5)
        self.buttonIndex = buttonIndex #Create associated "Edit" button for each expense entry 
        self.deleteButton = Button(frame, height = 1,
                 width = 10, 
                 text ="Delete",
                 command = lambda:deleteAndUpdate())
        self.editButton.grid(row = buttonIndex, column = 6) 
    def changeExpenseName(self, newName):
        self.expense = newName

    def changeExpenseAmount(self, newAmount):
        self.amount = newAmount
        self.yearlyCost = newAmount * 12

    def changeExpenseDate(self, newDate):
        self.monDueDate = newDate
    
    def updateExpense(self):
        print("Hello Update" + self.expense)
               
        


class ExpenseList:
    
    def __init__(self, frame:ttk.Frame, master:Tk):
        self.expenseList = []
        self.fileLoaded = False
        self.expenseFrame = frame
        self.addExpenseButton = Button(frame, height = 1, width = 20, text = "Add Expense", command=lambda:self.addExpenseClicked())
        self.addButtonIndex = 1 #Index in grid for the Add Expense button
        self.addExpenseButton.grid(row = self.addButtonIndex, column = 0)
        self.addExpenseButton.config(state="disabled") #Grey out the button until the profile is loaded by the user
        self.masterWindow = master
        self.deleteButton = Button(frame, height = 1, width = 20, text = "Delete Expense", command=lambda:self.deleteClicked())
        self.deleteButton.grid(row = self.addButtonIndex, column = 1)
        self.deleteButton.config(state="disabled") #Grey out the button until the profile is loaded by the user
        
        
    def deleteClicked(self):
        print("DELETING!!!!")
        editWin = Toplevel(self.masterWindow)
        editWin.title("Delete Expense")
        editWin.geometry("350x150")
        Label(editWin, text = "Expense to Delete :", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 5, padx = 10, pady = 25) 
        ###Load the users profile into the GUI
        n = StringVar() 
        expenseChosen = ttk.Combobox(window, width = 27, textvariable = n)
        
    def loadMonthlyExpense(self):
        rowCounter = 1
        counter = 0
        with open('monthlyExpenses.csv', 'r') as file:
            next(file)
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                print(counter)
                counter += 1
                self.expenseList.append(MonthlyExpense(line[0],line[1],line[2], rowCounter, self.expenseFrame))
                for i in range(0,4):
                    message = Message(self.expenseFrame, width = 100, text = line[i])
                    message.grid(row = rowCounter, column = i)
                
                rowCounter += 1
                print("check")

        self.addButtonIndex = rowCounter
        self.addExpenseButton.grid(row=self.addButtonIndex, column = 0)
        self.addExpenseButton.config(state="normal") #grey out the Add Expense button once the profile is loaded
        self.deleteButton.grid(row=self.addButtonIndex, column = 1)
        self.deleteButton.config(state="normal") #grey out the Add Expense button once the profile is loaded
            
        self.fileLoaded = True

        ### Action taken when the "Add Expense" button is clicked
    def addExpenseClicked(self):
        editWin = Toplevel(self.masterWindow)
        editWin.title("Add Monthly Expense")
        editWin.geometry("450x250")
        Label(editWin, text='Monthly Expense').grid(row=1)
        Label(editWin, text='Amount Due ($)').grid(row=2)
        Label(editWin, text='Day of Month Due').grid(row=3)
        expense = Entry(editWin)
        amount = Entry(editWin)
        date = Entry(editWin)
        
        expense.grid(row=1, column=1)
        amount.grid(row=2, column=1)
        date.grid(row=3, column=1)
                 
        Display = Button(editWin, height = 1,
                     width = 10, 
                     text ="Save",
                     command = lambda:self.addMonthlyExpense(expense.get(), amount.get(), date.get()))
        Display.grid(row=9,column=2)
        
        ###Saves CSV file with the list of expenses
    def saveMonthlyExpenses(self):
        counter = 0
        if self.fileLoaded == False:
            return 0
        with open('monthlyExpenses.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            field = ["EXPENSE", "MONTHLY COST", "MONTHLY DUE DATE", "YEARLY TOTAL COST"]
            
            writer.writerow(field)
            for i in self.expenseList:
                writer.writerow([i.expense, i.amount, i.monDueDate, i.yearlyCost])
        return 1
    
        ###Adds monthly expense to the list, adds an entry in the Monthly Expenses tab, and outputs to/resaves the csv file
    def addMonthlyExpense(self, expense, amount, date):

        self.addButtonIndex += 1
        newExpense = MonthlyExpense(expense, amount, date, self.addButtonIndex-1, self.expenseFrame)
        self.expenseList.append(newExpense)
        self.addExpenseButton.grid(row=self.addButtonIndex, column = 0)
        expenseMes = Message(self.expenseFrame, width = 100, text = expense)
        expenseMes.grid(row = self.addButtonIndex - 1, column = 0)
        amountMes = Message(self.expenseFrame, width = 100, text = amount)
        amountMes.grid(row = self.addButtonIndex - 1, column = 1)
        dateMes = Message(self.expenseFrame, width = 100, text = date)
        dateMes.grid(row = self.addButtonIndex - 1, column = 2)
        yearlyMes = Message(self.expenseFrame, width = 100, text = newExpense.yearlyCost)
        yearlyMes.grid(row = self.addButtonIndex - 1, column = 3)
        self.saveMonthlyExpenses()
        
'''class ExpenseWindow:
    def __init__(self, window:'''
                
'''testExpense = ExpenseList()
testExpense.loadMonthlyExpense()
#print(testExpense.expenseList[0].expense)
#newExpense = MonthlyExpense("Health Insurance", 200, 1)
#testExpense.addMonthlyExpense("Health Insurance", 200, 1)
#testExpense.saveMonthlyExpenses()
print(testExpense.expenseList[0].expense)   
testExpense.addMonthlyExpense("Rent", 1100, 1)
testExpense.saveMonthlyExpenses()
print(testExpense.expenseList[2].expense)   '''