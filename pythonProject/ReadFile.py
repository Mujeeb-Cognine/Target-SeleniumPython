file = open('test.txt')
# Read all the contents of file
# Read n number of characters by passing parameters.
# print(file.read(2))
# Read one single line at a time readline()
# print(file.readline())
# print(file.readline())

# print line by line using readline method
line = file.readline()
while line != "":
    print(line)
    line=file.readline()

# values = [mobiles, washingmachines, refrigerators]
# for line in file.readline():
#     print(line)


file.close()