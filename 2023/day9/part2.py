with open("input.txt", "r") as file:
    lines = file.readlines()


def dif(l):
    o = []
    for i in range(len(l[:-1])):
        o.append(l[i + 1] - l[i])
    return o


def gentree(seq):
    nlayer = list(seq)
    layers = [nlayer]
    while any(n != 0 for n in nlayer):
        nlayer = dif(nlayer)
        layers.append(nlayer)
    return layers


s = 0
for line in lines:
    t = gentree(map(int, line.split(" ")))
    for i, l in enumerate(reversed(t)):
        j = -(i + 1)
        if i == 0:
            l.insert(0, 0)
        try:
            t[j - 1].insert(0, t[j - 1][0] - l[0])
        except IndexError:
            s += t[0][0]
print(s)
