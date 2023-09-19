file = open('test.txt')
# Read all the context of file
# print(file.read())
# print(file.read(5)) # To read n number of characters by passing paramater

# To read one single line at a time readline()
# print(file.readline())
# print(file.readline())


# Print line by line using readline method
# line = file.readline()
# while line!="":
#     print(line)
#     line = file.readline()

for line in file.readlines():
    print(line)

file.close()
