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


cols = [[l[n] for l in lines] for n in range(len(lines[0]))]
cns = [ci for ci, c in enumerate(cols) if all(x == "." for x in c)]
rns = [ri for ri, r in enumerate(lines) if all(x == "." for x in r)]
# print(rns)

gs = []
for li, l in enumerate(lines):
    for ci, c in enumerate(l):
        if c == "#":
            gs.append(
                G(
                    ci + len([c for c in cns if c < ci]) * 999999,
                    li + len([r for r in rns if r < li]) * 999999,
                )
            )

# print(gs)
gcs = combinations(gs, r=2)
s = 0
for g1, g2 in gcs:
    s += abs(g1.x - g2.x) + abs(g2.y - g1.y)
print(s)
