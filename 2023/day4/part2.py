with open("input.txt", "r") as file:
    lines = file.readlines()

ncards = {n: 1 for n in range(len(lines))}

for index, line in enumerate(lines):
    for _ in range(ncards[index]):
        wnums = line.split(":")[1].split("|")[0]
        nums = line.split(":")[1].split("|")[1]
        wnums = [int(n) for n in wnums.split(" ") if n]
        nums = [int(n) for n in nums.split(" ") if n]

        rwnums = [num for num in nums if num in wnums]
        for i in range(index + 1, index + len(rwnums) + 1):
            ncards[i] += 1

print(sum(ncards.values()))
