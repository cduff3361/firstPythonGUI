import csv 


class MonthlyExpense:
    
    def __init__(self, expenseName, amount, monthlyDueDate):
        self.expense = expenseName
        self.amount = amount 
        self.monDueDate = monthlyDueDate
        self.yearlyCost = monthlyDueDate * 12
    
    def changeExpenseName(self, newName):
        self.expense = newName

    def changeExpenseAmount(self, newAmount):
        self.amount = newAmount
        self.yearlyCost = newAmount * 12

    def changeExpenseDate(self, newDate):
        self.monDueDate = newDate
               
        


class ExpenseList:
    
    def __init__(self):
        self.expenseList = []
        self.fileLoaded = False
        
    def loadMonthlyExpense(self):
        with open('monthlyExpenses.csv', 'r') as file:
            next(file)
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                self.expenseList.append(MonthlyExpense(line[0],line[1],line[2]))
        self.fileLoaded = True

    def saveMonthlyExpenses(self):
        
        if self.fileLoaded == False:
            return 0
        with open('monthlyExpenses.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            field = ["EXPENSE", "MONTHLY COST", "MONTHLY DUE DATE", "YEARLY TOTAL COST"]
            
            writer.writerow(field)
            for i in self.expenseList:
                writer.writerow([i.expense, i.amount, i.monDueDate, i.yearlyCost])
        return 1
        
    def addMonthlyExpense(self, expense, amount, date):
        newExpense = MonthlyExpense(expense, amount, date)
        self.expenseList.append(newExpense)
                
testExpense = ExpenseList()
testExpense.loadMonthlyExpense()
#print(testExpense.expenseList[0].expense)
#newExpense = MonthlyExpense("Health Insurance", 200, 1)
#testExpense.addMonthlyExpense("Health Insurance", 200, 1)
#testExpense.saveMonthlyExpenses()
print(testExpense.expenseList[0].expense)   
testExpense.addMonthlyExpense("Rent", 1100, 1)
testExpense.saveMonthlyExpenses()
print(testExpense.expenseList[2].expense)   