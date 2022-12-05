file = open("./input.txt")
lines = file.readlines()

crates = [[], [], [], [], [], [], [], [], []]
for line in lines[:8]:
    for i, col in enumerate(range(2, 36, 4)):
        crates[i].append(line[1 + 4 * i])

instructions = lines[10:]
for i, _ in enumerate(crates):
    if ' ' in crates[i]:
        crates[i] = [x for x in crates[i] if x != ' ']

inst = []
for i in instructions:
    inst.append(i.split('move ')[1].split(' from ')[0])
    inst.append(i.split('move ')[1].split(' from ')[1].split(' to ')[0])
    inst.append(i.split('move ')[1].split(' from ')[1].split(' to ')[1])
    for c in range(int(inst[0])):
        removed = crates[int(inst[1]) - 1].pop(int(inst[0]) - 1 - c)
        crates[int(inst[2]) - 1].insert(0, removed)
    inst = []

total = []
for col in crates:
    total.append(col[0])
print(total)
