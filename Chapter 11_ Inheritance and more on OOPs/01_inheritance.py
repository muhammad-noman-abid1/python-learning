class Employee: #  this is  Base class Or parent class
    company = "spaceX"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

#class Programmer:   # this is an old methed 
#   company = "Tesla"
#   def show(self):
#        print(f"The name is {self.name} and the salary is {self.salary}")
#
#    def showLanguage(self):
#        print(f"The name is {self.name} and is good with {self.language } language")
# more efficient method


class Programmer(Employee): # This is Derived class or child class , Now we can use all method and attributes of Employee class in this class automatically
    company = "Tesla"
    def showLanguage(self):
        print(f"The name is {self.company} and is good with {self.language } language")

a = Employee()
b = Programmer() 
print(a.company,b.company)