file = open("testfile.txt","w")
file.write("file text content")
file.close()

file = open("testfile.txt","r")
content=file.read()
file.close()
print(content)