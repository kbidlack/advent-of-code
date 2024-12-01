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
for (
    i,
    n,
) in enumerate(n1):
    s += abs(n - n2[i])

print(s)
