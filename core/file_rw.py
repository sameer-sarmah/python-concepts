content = '''
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
'''
fileName = "testfile.txt"

file = open(fileName, "w")
file.write(content)
file.close()

file = open(fileName, "r")
content = file.read()
file.close()
print(content)

'''
the with statement replaces a try-catch block with a concise shorthand. It also ensures closing resources right after processing them.
Therefore we need not "close" the file
'''

with open(fileName, "w") as file:
    file.write(content)

with open(fileName, "r") as file:
    content = file.read()
    print(content)
