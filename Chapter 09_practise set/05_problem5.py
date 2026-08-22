words = ["dog","donkey","bad","cat"]  # taking list of words  
 
with open("file.txt","r") as f:
    content = f.read() # reading the content of file
for word in words: 
    content = content.replace(word, "#" * len(word))  # replacing the content with # number of times lenght of word
  
with open("file.txt","w") as f:     # writing the new content in file 
    f.write(content)
