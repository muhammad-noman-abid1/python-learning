f=open("file.txt")
print(f.read())
f.close() 

# The same code can be written Using with statement like this:
with open("file.txt")as f:
    print(f.read())

# So now you don't have explicitly close the file by using f.close