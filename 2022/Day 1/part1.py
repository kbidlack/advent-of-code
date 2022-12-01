input = open('./input.txt')
lines = input.readlines()

elves = []
total = 0

for line in lines:
    if line == '\n':
        elves.append(total)
        total = 0
    else:
        total += int(line)

print(max(elves))
