with open("this.txt","r") as f:
    content = f.read()

with open("this__copy.txt","w")as f:
    f.write(content)