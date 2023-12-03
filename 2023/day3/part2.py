with open("input.txt", "r") as file:
    lines = file.readlines()

s = 0
rows = [line.replace("\n", "") for line in lines]

from dataclasses import dataclass


@dataclass
class Symbol:
    char: str
    x: int
    y: int
    nextto: list


def adj(pos1, pos2):
    if (abs(pos1[0] - pos2[0]) < 2) and (abs(pos1[1] - pos2[1]) < 2):
        return True
    else:
        return False


syms: list[Symbol] = []
for y, row in enumerate(rows):
    for x, char in enumerate(row):
        if not char.isdigit() and char != "\n" and char != ".":
            syms.append(Symbol(char, x, y, []))


for y, row in enumerate(rows):
    buf = []
    nums = []
    for i, n in enumerate(row + "\n"):
        if n.isdigit():
            buf.append(n)
        else:
            nums.append(("".join(buf), i))
            buf.clear()
    nums = [n for n in nums if n[0]]

    for num in nums:
        enumpos = num[1]
        numpos = num[1] - len(num[0])
        # numpos = row.find(num[0])
        # enumpos = numpos + len(num[0])
        # print(numpos, enumpos, num)
        for i in range(numpos, enumpos):
            for sym in [s for s in syms if s.char == "*"]:
                # print(sym)
                if adj((i, y), (sym.x, sym.y)):
                    if not num in sym.nextto:
                        sym.nextto.append(num)

for sym in syms:
    if len(sym.nextto) == 2:
        s += int(sym.nextto[0][0]) * int(sym.nextto[1][0])

print(s)
