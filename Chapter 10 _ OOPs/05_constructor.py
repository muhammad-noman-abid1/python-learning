class Employee:   
    language = "Py" 
    salary = 24000

    def __init__(self, name, salary, language): # _init_ is a dunder method function which called automatically
        self.name = name
        self.salary = salary
        self.language = language

        print("I am a dunder method so called automatically")

    def getinfo(self): # using functions in classes
        print(f"The salary of {self.name} is Rs:{self.salary} ")
    @staticmethod 
    def greet(): 
        print("Thank you")

# can be done like this If you want new object instance but you must have to call these in def _init function in the upper code
nomi = Employee("nomi",30000, "Javascript")
# nomi.name="nomi"
print(nomi.name,nomi.salary,nomi.language)

#  But from now you have to do the same work as in the previous object for adding the new object instance in an object
fawad = Employee("fawad",20000,"C++")
# fawad.name="fawad"
print(fawad.name,fawad.salary,fawad.language)



