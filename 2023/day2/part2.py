import re

with open("input.txt", "r") as file:
    lines = file.readlines()

s = 0
for index, line in enumerate(lines):
    g = index + 1
    reds = re.findall(r"\d* red", line)
    blues = re.findall(r"\d* blue", line)
    greens = re.findall(r"\d* green", line)
    # print(line.replace("\n", ""))
    # print(reds + blues + greens)
    numsreds = [
        int(num) for num in map(lambda x: "".join(c for c in x if c.isdigit()), reds)
    ]
    numsblues = [
        int(num) for num in map(lambda x: "".join(c for c in x if c.isdigit()), blues)
    ]
    numsgreens = [
        int(num) for num in map(lambda x: "".join(c for c in x if c.isdigit()), greens)
    ]

    s += max(numsreds) * max(numsblues) * max(numsgreens)

print(s)
