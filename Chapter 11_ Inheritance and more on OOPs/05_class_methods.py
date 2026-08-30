class Employee:
    a = 11
    @classmethod  # Class method decorator is used to call the value of class attribute instead of instance attribute as it will call the value of instance attribute by default 
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 50
e.show()