with open("input.txt", "r") as file:
    lines = file.readlines()

n1 = []
n2 = []

for line in lines:
    n1.append(int(line.split(" ")[0]))
    n2.append(int(line.split(" ")[-1]))
n1.sort()
n2.sort()

s = 0
for n in n1:
    s += n * n2.count(n)
print(s)
