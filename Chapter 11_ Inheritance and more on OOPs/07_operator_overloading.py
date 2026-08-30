class Number:
    def __init__(self,n):
        self.n = n 

    def __add__(self, num):
        return self.n + num.n
    
    def __sub__(self, num):
        return self.n - num.n
    
    def __mul__(self, num):
        return self.n * num.n
    
    def __truediv__(self, num):
        return (self.n / num.n)
            

n = Number(int(input("Enter first number: ")))
m = Number(int(input("Enter second number: ")))
print(n+m)
print(n-m)
print(n*m)
print(n / m)