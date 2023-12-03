with open("input.txt", "r") as file:
    lines = file.readlines()

s = 0
rows = [line.replace("\n", "") for line in lines]
syms = []

from dataclasses import dataclass


@dataclass
class Symbol:
    char: str
    x: int
    y: int


for y, row in enumerate(rows):
    for x, char in enumerate(row):
        if not char.isdigit() and char != "\n" and char != ".":
            syms.append(Symbol(char, x, y))


def adj(pos1, pos2):
    if (abs(pos1[0] - pos2[0]) < 2) and (abs(pos1[1] - pos2[1]) < 2):
        return True
    else:
        return False


for y, row in enumerate(rows):
    buf = []
    nums = []
    for i, n in enumerate(row + "\n"):
        if n.isdigit():
            buf.append(n)
        else:
            nums.append(("".join(buf), i))
            buf.clear()
    # nums = ["".join([c for c in num if c.isdigit()]) for num in row.split(".")]
    nums = [n for n in nums if n[0]]

    for num in nums:
        enumpos = num[1]
        numpos = num[1] - len(num[0])
        # numpos = row.find(num[0])
        # enumpos = numpos + len(num[0])
        # print(numpos, enumpos, num)
        for i in range(numpos, enumpos):
            if any(adj((i, y), (sym.x, sym.y)) for sym in syms):
                s += int(num[0])
                break
        else:
            pass
            # print(num, numpos, y)

    # print(row, nums)

print(s)
