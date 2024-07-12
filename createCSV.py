import csv


with open('monthlyExpenses.csv', 'w', newline='') as fileWriteFirst:
    writer = csv.writer(fileWriteFirst)
    field = ["EXPENSE", "MONTHLY COST", "MONTHLY DUE DATE", "YEARLY TOTAL COST"]
    
    writer.writerow(field)
    writer.writerow(['', '', '',''])