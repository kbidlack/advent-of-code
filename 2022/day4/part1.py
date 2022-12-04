f = open('./input.txt')
l = f.readlines()
t = 0

for line in l:
    h1, h2 = line.split(',')
    h1n1, h1n2 = h1.split('-')
    h2n1, h2n2 = h2.split('-')

    if (int(h1n1) <= int(h2n1)) and (int(h1n2) >= int(h2n2)):
        t += 1
        print(h1n1, h1n2, h2n1, h2n2)
    elif (int(h2n1) <= int(h1n1)) and (int(h2n2) >= int(h1n2)):
        t += 1
        print(h1n1, h1n2, h2n1, h2n2)
    else:
        continue

    
print(t)
