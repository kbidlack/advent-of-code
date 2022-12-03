import math

f = open('./input.txt')
l = f.readlines()
total = 0

def p(thing):
    if thing.lower() == thing:
        return ord(thing) - 96
    elif thing.upper() == thing:
        return ord(thing) - 38

for line in l:
    h1, h2 = line[:math.floor(len(line)/2)], line[math.floor(len(line)/2):]
    for char1 in h1:
        for char2 in h2:
            if char1 == char2:
                c = char1
                print(c)
                print(p(c))
                print(h1, h2)
            else:
                continue
    total += p(c)

print(total)
