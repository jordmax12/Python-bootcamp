jabber = open("../data/sample.txt", "r")

# print line by line
for line in jabber:
    print(line)

# print whole thing


jabber.close()

# method dont have to use close
# with open("../data/sample.txt", "r") as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

with open("../data/sample.txt", "r") as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline() # once this doesnt have a line to read
        # it will return empty string, thus terminates while loop

with open("../data/sample.txt", "r") as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines:
    print(line, end='')

for line in lines[::-1]:
    print(line, end='')