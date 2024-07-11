import csv

class Profile:
    
    def __init__(self):
        with open('profiles1.csv', 'r') as fileRead:
            reader = csv.reader(fileRead, delimiter=',')
            row0 = next(reader)
            row1 = next(reader)
            self.firstName = row1[0]
            self.middleName = row1[1]
            self.lastName = row1[2]
            self.monthlyBudget = row1[3]

            
    def printInfo(self):
        print(self.firstName + ' ' + self.middleName + ' ' + self.lastName + ' ' + '$' + str(self.monthlyBudget))

    def changeMonBud(self, monthlyBudget):
        if monthlyBudget >= 0:
            self.monthlyBudget = monthlyBudget
        else:
            self.monthlyBudget = 0
    
    def changeFirstName(self, first):
        self.firstName = first
        with open('profiles1.csv', 'w', newline='') as fileWriteFirst:
            writer = csv.writer(fileWriteFirst)
            field = ["FIRST", "MIDDLE", "LAST","MONTHLY BUDGET"]
            
            writer.writerow(field)
            writer.writerow([self.firstName, self.middleName, self.lastName, self.monthlyBudget])
            
    
    def changeMiddleName(self, middle):
        self.middleName = middle
        with open('profiles1.csv', 'w', newline='') as fileWriteFirst:
            writer = csv.writer(fileWriteFirst)
            field = ["FIRST", "MIDDLE", "LAST","MONTHLY BUDGET"]
            
            writer.writerow(field)
            writer.writerow([self.firstName, self.middleName, self.lastName, self.monthlyBudget])
            
    def changeLastName(self, last):
        self.lastName = last
        with open('profiles1.csv', 'w', newline='') as fileWriteFirst:
            writer = csv.writer(fileWriteFirst)
            field = ["FIRST", "MIDDLE", "LAST","MONTHLY BUDGET"]
            
            writer.writerow(field)
            writer.writerow([self.firstName, self.middleName, self.lastName, self.monthlyBudget]) 
    def getFirstName(self):
        return self.firstName
    def getMiddleName(self):
        return self.middleName
    def getLastName(self):
        return self.lastName
    def getMonBud(self):
        return self.monthlyBudget       
        
'''firstProfile = Profile()
firstProfile.printInfo()
firstProfile.changeMonBud(5000)
firstProfile.changeFirstName('Chi')
firstProfile.printInfo()
firstProfile.changeMiddleName('Joep')
firstProfile.printInfo()
firstProfile.changeLastName('Du')
firstProfile.printInfo()'''