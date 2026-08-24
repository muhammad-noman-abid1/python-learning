class demo:
    a=5

b = demo()
print(b.a) # Prints the class attribute because instance attribute is not present
b.a = 1  # Now I have assigned instance attribute
print(b.a) # Here it will print instance attribute because I have assigned it the instance attribute 
print(demo.a) # Now as I call the class attribute so it will print 5
 