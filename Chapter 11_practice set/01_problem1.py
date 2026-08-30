class twoDvector:
    def __init__(self, i ,j ):
        self.i = i
        self.j = j 
    def show(self):
        print(f"The 2D vector is: {self.i}i + {self.j}j")

class threeDvector(twoDvector):
    def __init__(self, i , j , k ):
        super().__init__(i , j)  
        self.k = k
    def show(self):
        print(f"The 3D vector is: {self.i}i + {self.j}j + {self.k}k")

a = twoDvector(int(input("Enter Num1: ")),( input("Enter Num2: ")))
b = threeDvector(int(input("Enter Num3: ")),(input("Enter Num4: ")),(input("Enter Num5: ")))
a.show()
b.show()


        