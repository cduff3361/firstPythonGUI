import csv


"""
Profile is a class that represents a user with the following info:
    -Name (First and Last)
    -Monthly Budget
This class also has a corresponding csv file which stores the profile information. Therefore, this class also handles
saving a profile when a change is made in the window
"""
class Profile:
    
    def __init__(self):
        with open('profiles1.csv', 'r') as fileRead:
            reader = csv.reader(fileRead, delimiter=',')
            row0 = next(reader)
            row1 = next(reader)
            self.firstName = row1[0] #Set the first name instance variable from the csv file
            self.middleName = row1[1] #Set the middle name instance variable from the csv file
            self.lastName = row1[2] #Set the last name instance variable from the csv file
            self.monthlyBudget = row1[3] #Set the monthly budget instance variable from the csv file 

            
    def printInfo(self):
        print(self.firstName + ' ' + self.middleName + ' ' + self.lastName + ' ' + '$' + str(self.monthlyBudget))

    """
    changeMonBud - update the monthly budget with input parameter monthlyBudget. Also save the csv file with new info
    """
    def changeMonBud(self, monthlyBudget):
        if monthlyBudget >= 0:
            self.monthlyBudget = monthlyBudget
            with open('profiles1.csv', 'w', newline='') as fileWriteFirst:
                writer = csv.writer(fileWriteFirst)
                field = ["FIRST", "MIDDLE", "LAST","MONTHLY BUDGET"]
                
                writer.writerow(field)
                writer.writerow([self.firstName, self.middleName, self.lastName, self.monthlyBudget])            
        else:
            self.monthlyBudget = 0

    """
    changeFirstName - update the first name with input parameter first. Also save the csv file with new info
    """    
    def changeFirstName(self, first):
        self.firstName = first
        with open('profiles1.csv', 'w', newline='') as fileWriteFirst:
            writer = csv.writer(fileWriteFirst)
            field = ["FIRST", "MIDDLE", "LAST","MONTHLY BUDGET"]
            
            writer.writerow(field)
            writer.writerow([self.firstName, self.middleName, self.lastName, self.monthlyBudget])
            
 
    """
    changeMiddleName - update the middle name with input parameter middle. Also save the csv file with new info
    """    
    def changeMiddleName(self, middle):
        self.middleName = middle
        with open('profiles1.csv', 'w', newline='') as fileWriteFirst:
            writer = csv.writer(fileWriteFirst)
            field = ["FIRST", "MIDDLE", "LAST","MONTHLY BUDGET"]
            
            writer.writerow(field)
            writer.writerow([self.firstName, self.middleName, self.lastName, self.monthlyBudget])

    """
    changeLastName - update the first name with input parameter last. Also save the csv file with new info
    """                
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
        