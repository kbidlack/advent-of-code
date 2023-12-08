with open("input.txt", "r") as file:
    lines = file.readlines()

insts = lines[0].strip()
nodes = {}
for line in lines[2:]:
    x = line.split("=")[0].strip()
    y = line.split("=")[1].strip().removeprefix("(").removesuffix(")").split(",")
    y[1] = y[1].strip()
    nodes.update({x: tuple(y)})


class Instructions(str):
    def __init__(self, s):
        self.pos = 0
        self.s = s

    def __iter__(self):
        return self

    def __next__(self):
        try:
            x = self.s[self.pos]
        except IndexError:
            self.pos = 0
            x = self.s[self.pos]
        self.pos += 1
        return x


insts = Instructions(insts)

ni = 0
nis = []
nnodes = [node for node in nodes.keys() if node.endswith("A")]
for j in range(6):
    ni = 0
    nnodes = [node for node in nodes.keys() if node.endswith("A")]
    nnodes = [nnodes[j]]
    insts = Instructions(insts.s)
    while True:
        inst = next(insts)
        i = 1 if inst == "R" else 0
        if all(node.endswith("Z") for node in nnodes):
            break
        nnodes = [nodes[node][i] for node in nnodes]
        ni += 1
    nis.append(ni)
import math

print(math.lcm(*nis))
