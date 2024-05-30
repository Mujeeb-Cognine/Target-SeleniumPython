#READ operation
file = open("test for R&W")
#print(file.read()) #read the txt with specific characters
print(file.readline())
# print(file.readline())

#print line by line by using while loop

line = file.readline()
while line !="":
    print(line)
    line = file.readline()

# other way
for line in file.readlines():
    print(line)

file.close()

#need to learn skip function to skip the particular lines
import itertools
with open ('file text','r') as f:
    next(f)
    for line in f:
        print(line)
