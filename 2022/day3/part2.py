import math

f = open('./input.txt')
l = f.readlines()
total = 0

def p(thing):
    if thing.lower() == thing:
        return ord(thing) - 96
    elif thing.upper() == thing:
        return ord(thing) - 38

lg = 0
for index, line in enumerate(l):
    if index % 3 == 0:
        lg += 1
        l1 = line
    elif index % 3 == 1:
        l2 = line
    elif index % 3 == 2:
        l3 = line
        for char1 in l1:
            for char2 in l2:
                for char3 in l3:
                    if (char1 == char2) and (char2 == char3) and char1 != '\n':
                        c = char1
                        print(c, p(c))
        total += p(c)
    
print(total)
