class Calculator:
    def __init__(self,n):
     self.n = n

    @staticmethod
    def greet():
       print("Hello!")
    
    def square(self):
        print(f"The square is: {self.n*self.n}")

    def cube(self):
        print(f"The square is: {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The square is: {self.n**1/2}")

    @staticmethod
    def greet1():
       print("Thank you!")

a = Calculator(5)
a.greet()
a.square()
a.cube()
a.squareroot()
a.greet1()












