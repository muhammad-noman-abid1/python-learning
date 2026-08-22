f = open("poem.txt")  # it will open the selected file
content = f.read() # it will read the whole file 

if ("twinkle" in content ): # condition 
    print("The word Twinkle is present in poem ") # if twinkle is present in file it will print that

else:
    print("The word Twinkle is not present in poem ")

f.close()