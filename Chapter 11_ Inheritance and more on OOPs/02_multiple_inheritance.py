# Here is the method for using multiple parent classes for a  derived class

class Employee: 
    company = "spaceX"
    name = "nomi"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")

class coder:
    language = "Python"
    def printLanguage(self):
        print(f" Out of all languages here is your language: {self.language}")


class Programmer(Employee, coder): #  This is a derived class from Multiple parents
    company = "Tesla"
    def showLanguage(self):
        print(f"The company is {self.company} and is good with {self.language } language")

a = Employee()
b = Programmer() 

b.show()
b.printLanguage()
b.showLanguage()
