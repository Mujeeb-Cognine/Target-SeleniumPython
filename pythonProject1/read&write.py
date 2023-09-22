# file = open("text.txt")

# print(file.read(5))

# print(file.readline())
# print(file.readline())
# print(file.readline())


# printing all the lines using FOR loop
# for line in file.readlines():
#
#          print(line)

line = file.readline()
while line != "":
    print(line)
    line = file.readline()

# file.close()