class Employee:   
    name= "nomi"   # these are class attributes
    language = "Py" # Class attributes will work for every object in which we use the class attribute
    salary = 24000

    def getinfo(self): # using functions in classes
        print(f"The salary of {self.name} is {self.salary} ")
    @staticmethod # is a decorator used inside a class to create a method that doesn't need access to the object (self) or the class (cls). 
    def greet():  # now greet is a staticmethod function so it doesn't need object or class data → no self/cls
        print(f"Thanks for being a developer")

nomi = Employee()   

print(nomi.name,nomi.language,nomi.salary)
nomi.getinfo()
Employee.greet() 