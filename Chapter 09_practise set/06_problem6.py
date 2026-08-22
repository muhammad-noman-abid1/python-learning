with open("log.txt")as f:
    content = f.read()

if ("python" in content):
    print("Yes! Python is present in the file")
else:
    print ("Python is not present in file")