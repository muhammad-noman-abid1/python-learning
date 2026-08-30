class Employee:
    a = 11
    @classmethod 
    def show(cls):
        print(f"The class attribute of a is {cls.a}")
    @property # allows you to use a method like an attribute, without calling it with ().
    def name(self):
        return f"First name is {self.fname} and second name is {self.Lname}"


    @name.setter  # is used with @property to control what happens when you assign a new value to a property.
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.Lname = value.split(" ")[1]

    
e = Employee()
e.a = 50
e.name= "Nomi Khan"
print(e.name)
e.show()