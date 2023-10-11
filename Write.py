#WRITE operation

with open("test for R&W",'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open("test for R&W",'w') as writer:
        for line in reversed(content):
            writer.write(line)
