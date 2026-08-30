class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"

# Test the implementation
v1 = Vector(int(input("Enter Num1 for v1: ")),(int(input("Enter Num2 for v1: "))),(int(input("Enter Num3 for v1: "))))
v2 = Vector(int(input("Enter Num1 for v2: ")),(int(input("Enter Num2 for v2: "))),(int(input("Enter Num3 for v2: "))))
v3 = Vector(int(input("Enter Num1 for v3: ")),(int(input("Enter Num2 for v3: "))),(int(input("Enter Num3 for v3: "))))  

print(v1 + v2)  
print(v1 * v2)

print(v1 + v3)  
print(v1 * v3)
