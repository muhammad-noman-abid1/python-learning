class Employee:
    def __init__(self):
        print("Constructor of Employee")
    name = "nomi"

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    lan = "python"

class Manager(Programmer):
    def __init__(self):
# Superclass is used derive any property from the previous class
        super().__init__() # This is a super class used to print the specific things Manager class as well as Programmer class
        print("Constructor of Manager")
    man = "noman"

# o = Programmer()
# print(o.name, o.lan)

o = Manager()
print(o. man)