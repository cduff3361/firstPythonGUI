import csv 
from tkinter import ttk
from tkinter import *



"""
class MonthlyExpense 

Monthly expense defined by a user that has the following:
    Expense Name
    Expense Amount 
    Day of the month the expense is due
    Total yearly cost
"""
class MonthlyExpense:
    
    def __init__(self,expenseName,amount,monthlyDueDate,buttonIndex,frame:ttk.Frame, master:Tk):
        self.expense = expenseName
        self.amount = int(amount) 
        self.monDueDate = monthlyDueDate
        self.yearlyCost = int(amount) * 12
        self.masterWindow = master
        #Associated edit button for each expense 
        '''self.editButton = Button(frame, height = 1,
                 width = 10, 
                 text ="Edit",
                 command = lambda:self.updateExpense())
        self.editButton.grid(row = buttonIndex, column = 5)
        self.buttonIndex = buttonIndex #Create associated "Edit" button for each expense entry '''
        '''self.deleteButton = Button(frame, height = 1,
                 width = 10, 
                 text ="Delete",
                 command = lambda:deleteAndUpdate())'''
        #self.editButton.grid(row = buttonIndex, column = 6) 
        
    def changeExpenseName(self, newName):
        self.expense = newName

    def changeExpenseAmount(self, newAmount):
        self.amount = newAmount
        self.yearlyCost = newAmount * 12

    def changeExpenseDate(self, newDate):
        self.monDueDate = newDate
    
    def updateExpense(self):
        print("Hello Update" + self.expense)
        editWin = Toplevel(self.masterWindow)
        editWin.title("Edit Expense")
        editWin.geometry("350x150")
        Label(editWin, text = "Expense to Delete :", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 5, padx = 10, pady = 25) 
        
        
    #def reloadEditButton(self):
        
               
        

"""
ExpenseList is a list of expenses. Also handles deleting expenses and adding expenses in the monthly expense tab/frame
"""
class ExpenseList:
    
    def __init__(self, frame:ttk.Frame, master:Tk):
        self.expenseList = []
        self.fileLoaded = False
        self.expenseFrame = frame
        self.monthlySum = int(0)
        self.addExpenseButton = Button(frame, height = 1, width = 20, text = "Add Expense",command=lambda:self.addExpenseClicked())
        self.addButtonIndex = 1 #Index in grid for the Add Expense button
        self.addExpenseButton.grid(row = self.addButtonIndex, column = 0)
        self.addExpenseButton.config(state="disabled") #Grey out the button until the profile is loaded by the user
        self.masterWindow = master
        self.deleteButton = Button(frame, height = 1, width = 20, text = "Delete Expense", command=lambda:self.deleteClicked())
        self.deleteButton.grid(row = self.addButtonIndex, column = 1)
        self.deleteButton.config(state="disabled") #Grey out the button until the profile is loaded by the user
        self.editButton = Button(frame, height = 1, width = 20, text = "Edit Expense", command=lambda:self.editClicked())
        self.editButton.grid(row = self.addButtonIndex, column = 2)
        self.editButton.config(state="disabled") #Grey out the button until the profile is loaded by the user
        
        
    """
    deleteClicked handles when the delete button is clicked. The result is a pop up window with a combobox to select which 
    monthly expense to delete. 
    """
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
        comboBoxVals = []
        
        
        
        for expenses in self.expenseList:
            comboBoxVals.append(expenses.expense)
        expenseChosen = ttk.Combobox(editWin, width = 27, textvariable = n, values = comboBoxVals)
        expenseChosen.grid(column=1, row =5)
        confirmButton = Button(editWin, height = 1, width = 20, text = "Delete Expense", command=lambda:self.confirmClicked(expenseChosen.get(), editWin))
        confirmButton.grid(column = 1, row = 10)
        
    """
    confirmClicked takes two arguments:
        expense - the the name of the expense chosen
        window - pop up window object 
        
    This method takes action when the user selects and then confirms the deletion of a monthly expense. The following occurs once confirmed:
        -Deletes the expense from the list 
        -Saves the new list to the csv
        -Clears the frame
        -Updates the frame with (now) one less monthly expense 
        -Destroys the pop up window 
    """
    def confirmClicked(self, expense, window:Toplevel):
        if expense != -1:
            counter = 0
            for i in self.expenseList:
                if i.expense == expense:
                    del self.expenseList[counter]
                    self.saveMonthlyExpenses()
                    self.clear_frame()
                    self.loadMonthlyExpense()
                    window.destroy()
                    
                    return
                else:
                    counter +=1
            self.saveMonthlyExpenses()
        print("ARE YOU SURE")
        
        
    """
    clear_frame clears all widgets from the monthly expense frame besides the add expense button and the delete button.
    """
    def clear_frame(self):
        #widgetList = self.expenseFrame.winfo_children();
        #print(widgetList[0:-1])
        for widgets in self.expenseFrame.winfo_children():
            #print(widgets._name)
            if widgets._name != self.addExpenseButton._name and widgets._name != self.deleteButton._name:
                widgets.destroy() 
        self.expenseList.clear()

        
            
    """
    loadMonthlyExpenses loads the csv file with monthly expenses and displays each into the monthly expense frame.
    """
    def loadMonthlyExpense(self):
        rowCounter = 1
        counter = 0
        self.addButtonIndex = 1
        self.monthlySum = 0
        currentAmount = 0
        if self.fileLoaded == True: #Need to rewrite the header after deleting expenses since the window gets cleared
            Label(self.expenseFrame, text = 'Monthly Expense', width = 20, bg = 'yellow').grid(row=0, column=0)
            Label(self.expenseFrame, text = 'Amount Due ($)', width = 20, bg = 'yellow').grid(row=0,column=1)
            Label(self.expenseFrame, text = 'Day of Month Due', width = 20, bg = 'yellow').grid(row=0,column=2)
            Label(self.expenseFrame, text = 'Yearly Cost ($)', width = 20, bg = 'yellow').grid(row=0,column=3)
        with open('monthlyExpenses.csv', 'r') as file:
            next(file)
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                counter += 1
                currentAmount = int(line[1])
                self.monthlySum = self.monthlySum + currentAmount
                #if self.fileLoaded == False:
                self.expenseList.append(MonthlyExpense(line[0],line[1],line[2], rowCounter, self.expenseFrame, self.masterWindow))
                for i in range(0,4):
                    message = Message(self.expenseFrame, width = 100, text = line[i])
                    message.grid(row = rowCounter, column = i)

                
                rowCounter += 1 #Update the row for the grid in the frame               

        self.addButtonIndex = rowCounter+1
        Label(self.expenseFrame, text = 'Total Monthly ($):', width = 20, bg = 'yellow').grid(row = self.addButtonIndex - 1, column = 0)
        Label(self.expenseFrame, text = self.monthlySum, width = 20, bg = 'yellow').grid(row = self.addButtonIndex - 1, column = 1)
        self.addExpenseButton.grid(row=self.addButtonIndex, column = 0)
        self.addExpenseButton.config(state="normal") #grey out the Add Expense button once the profile is loaded
        self.deleteButton.grid(row=self.addButtonIndex, column = 1)
        self.deleteButton.config(state="normal") #grey out the Add Expense button once the profile is loaded
        self.editButton.grid(row=self.addButtonIndex, column = 2)
        self.editButton.config(state="normal") #grey out the Add Expense button once the profile is loaded        
            
        self.fileLoaded = True


    def editClicked(self):
        editWin = Toplevel(self.masterWindow)
        editWin.title("Edit Expense")
        editWin.geometry("350x150")
        Label(editWin, text = "Expense to Edit :", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 5, padx = 10, pady = 25) 
        ###Load the users profile into the GUI
        n = StringVar() 
        comboBoxVals = []
        
        
        
        for expenses in self.expenseList:
            comboBoxVals.append(expenses.expense)
        expenseChosen = ttk.Combobox(editWin, width = 27, textvariable = n, values = comboBoxVals)
        expenseChosen.grid(column=1, row =5)
        
        Label(editWin, text = "Expense Name: ").grid(column = 0, row = 7, padx = 10)
        Label(editWin, text = "Expense Amount ($): ").grid(column = 0, row = 8, padx = 10)
        Label(editWin, text = "Expense Due Date: ").grid(column = 0, row =9, padx = 10)   

        nameEdit = Entry(editWin)
        nameEdit.grid(column = 1, row = 7)
        nameEdit.insert(0, expenseChosen.get())
        amountEdit = Entry(editWin).grid(column = 1, row = 8)
        dateEdit = Entry(editWin).grid(column = 1, row = 9)
        
        #loadButton = Button(editWin, height = 1, width = 20, text = "vv", command =  
        
        confirmButton = Button(editWin, height = 1, width = 20, text = "Save Expense", command=lambda:self.confirmClicked(expenseChosen.get(), editWin))
        confirmButton.grid(column = 1, row = 10)        
    """
    addExpenseClicked is the action taken when the "Add Expense" button is clicked:
        -Pops up a window for the user to input information about the new expense. 
    """
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
        
     
    """
    saveMonthlyExpenses saves CSV file with the list of expenses
    """
    def saveMonthlyExpenses(self):
        counter = 0
        if self.fileLoaded == False: #Don't save anything until the user has loaded their profile
            return 0
        with open('monthlyExpenses.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            field = ["EXPENSE", "MONTHLY COST", "MONTHLY DUE DATE", "YEARLY TOTAL COST"]
            
            writer.writerow(field)
            for i in self.expenseList:
                writer.writerow([i.expense, i.amount, i.monDueDate, i.yearlyCost])
        return 1
    
    """
    addMonthlyExpense adds a monthly expense to the list, adds an entry in the Monthly Expenses tab, and outputs to/resaves the csv file
    """
    def addMonthlyExpense(self, expense, amount, date):

        self.addButtonIndex += 1
        newExpense = MonthlyExpense(expense, amount, date, self.addButtonIndex-1, self.expenseFrame)
        self.expenseList.append(newExpense)
        self.addExpenseButton.grid(row=self.addButtonIndex, column = 0)
        self.deleteButton.grid(row = self.addButtonIndex, column = 1)
        expenseMes = Message(self.expenseFrame, width = 100, text = expense)
        expenseMes.grid(row = self.addButtonIndex - 1, column = 0)
        amountMes = Message(self.expenseFrame, width = 100, text = amount)
        amountMes.grid(row = self.addButtonIndex - 1, column = 1)
        dateMes = Message(self.expenseFrame, width = 100, text = date)
        dateMes.grid(row = self.addButtonIndex - 1, column = 2)
        yearlyMes = Message(self.expenseFrame, width = 100, text = newExpense.yearlyCost)
        yearlyMes.grid(row = self.addButtonIndex - 1, column = 3)
        self.saveMonthlyExpenses()
        
