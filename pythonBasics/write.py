# file = open("test.txt")
#
# file.close()

# Read the file and store all the lines in list
# Reverse the list
# write the list back to the file
with open('test.txt', 'r') as reader:
    content = reader.readlines() #[abc,bjhfc,cat,dog,elephant]
    reversed(content) ##[elephant,dog,cat,bjhfc,abc]
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)