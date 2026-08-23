class Employee:   
    name= "nomi"   # these are class attributes
    language = "Py"
    salary = 24000

    def getinfo(self): # using functions in classes
        print(f"The salary of {self.name} is {self.salary} and Programming language is {self.language} ")

    def greet(self):
        print(f"Thanks for being a {self.language} developer")


nomi = Employee()   # this is an object , here nomi is an object 
nomi.language = "javascript" # instance attribute will print out because instance attribute take preference over class attributes
print(nomi.name,nomi.language,nomi.salary)
nomi.getinfo()  # calling the function
# can also be written as Employee.getinfo(nomi)
nomi.greet() 


