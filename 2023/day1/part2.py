import re

with open("input.txt", "r") as file:
    lines = file.readlines()

s = 0

ns = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

for line in lines:
    nums = list(
        map(
            lambda x: str(ns.get(x) or x),
            re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line),
        )
    )
    n = nums[0] + nums[-1]
    s += int(n)

print(s)
