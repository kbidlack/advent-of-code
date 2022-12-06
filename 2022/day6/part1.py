with open('./input.txt') as file:
    stuff = file.read()

buf = []
for index, char in enumerate(stuff):
    if len(buf) == 4:
        buf.pop(0)
    buf.append(char)
    if len(set(buf)) == len(buf):
        print(buf, index)

