

with open("log.txt")as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if ("python" in line):
        print(f"Yes! Python is present in the file in line number: {lineno}")
        break
    lineno +=1 
   
else:
    print ("No! Python is not present in file")
