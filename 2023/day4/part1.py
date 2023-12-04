with open("input.txt", "r") as file:
    lines = file.readlines()

s = 0

for line in lines:
    wnums = line.split(":")[1].split("|")[0]
    nums = line.split(":")[1].split("|")[1]
    wnums = [int(n) for n in wnums.split(" ") if n]
    nums = [int(n) for n in nums.split(" ") if n]

    rwnums = [num for num in nums if num in wnums]
    if rwnums:
        score = 2 ** (len(rwnums) - 1)
    else:
        score = 0
    # print(wnums, nums, line.replace("\n", ""))
    s += score

print(s)
