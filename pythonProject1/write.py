# file = open("text.txt")
#
# file.close()

with open('text.txt','r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('text.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
            with open('text.txt', 'w') as writer1:
                for line1 in reversed(content):
                    writer1.write(line1)


