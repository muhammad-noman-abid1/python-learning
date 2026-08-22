with open("file1.txt","r") as f:
    content1 = f.read()

with open("file2.txt","r") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes! These files are identical")

else:
    print("No! These files are not identical.")