f = open('./input.txt')
l = f.readlines()
t = 0

for line in l:
    h1, h2 = line.split(',')
    h1n1, h1n2 = h1.split('-')
    h2n1, h2n2 = h2.split('-')

    h1set = set(range(int(h1n1), int(h1n2) + 1))
    h2set = set(range(int(h2n1), int(h2n2) + 1))
    if h1set.intersection(h2set):
        t += 1

print(t)
