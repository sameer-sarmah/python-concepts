fileName = "testfile.txt"
size = 128

def read_file(file_name:str, chunk_size:int = 512):
    with open(fileName, "rb") as file:
        while segment := file.read(size):
            yield segment

for segment in read_file(fileName,size):
    print(segment)