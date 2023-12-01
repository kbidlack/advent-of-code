with open("input.txt", "r") as file:
    lines = file.readlines()

s = 0

for line in lines:
    num = "".join(char for char in line if char.isdigit())
    n = num[0] + num[-1]
    s += int(n)

print(s)
