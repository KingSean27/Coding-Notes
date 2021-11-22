# you can open a text file and read it with python
# you can interact with it in many ways, including as a list 

print("\nReading characters from the file.")
text_file = open("read_it.txt", "r")
print(text_file.read(1))
print(text_file.read(5))


lines = text_file.readlines()

for line in lines:
    print (line)



text_file.close()