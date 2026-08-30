class Complex: # This program is used to print the real and imaginary part  of a complex numbers
    def __init__(self, r , i ):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return Complex(self.r + c2.r , self.i + c2.i)

    def __str__(self):
        return f"{self.r} + {self.i}i"

c1 = Complex(int(input("Enter Num1: ")),(int(input("Enter Num2: "))))
c2 = Complex(int(input("Enter Num3: ")),(int(input("Enter Num4: "))))
print(c1 + c2)