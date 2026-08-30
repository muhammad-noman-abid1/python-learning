# do more practise on that classes

class Employee:
    name = "nomi"

class Programmer(Employee):
    lan = "python"

class Manager(Programmer):
    man = "noman"

o = Employee()
print(o.name) # prints the name attribute
# Print(o.lan) # It will show error because there is no lan attribute in the Employee class

o = Programmer()
print(o.name, o.lan)

o = Manager()
print(o.name, o.lan , o.man)