with open("input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

from dataclasses import dataclass
from itertools import combinations


@dataclass
class G:
    x: int
    y: int

    def __neq__(self, other):
        return not self.x == other.x and self.y == other.y


rows = []
for line in lines:
    rows.append(list(line))
    if all(c == "." for c in line):
        rows.append(list(line))

cols = [[l[n] for l in lines] for n in range(len(rows[0]))]
cns = [ci for ci, c in enumerate(cols) if all(x == "." for x in c)]

nrows = []
for row in rows:
    nr = ""
    for ci, c in enumerate(row):
        nr += c
        if ci in cns:
            nr += "."
    nrows.append(nr)

gs = []
for li, l in enumerate(nrows):
    for ci, c in enumerate(l):
        if c == "#":
            gs.append(G(ci, li))

# print(gs)
gcs = combinations(gs, r=2)
s = 0
for g1, g2 in gcs:
    s += abs(g1.x - g2.x) + abs(g2.y - g1.y)
print(s)
