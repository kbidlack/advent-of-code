with open('input.txt', 'r') as file:
    lines = file.readlines()

trees: list[list] = []

for line in lines:
    trees.append([int(char) for char in line if char != '\n'])

scenic_score = 0
max_scenic_score = 0

for rindex, row in enumerate(trees):
    for tindex, tree in enumerate(row):
        left = 0
        right = 0
        top = 0
        bottom = 0

        if (tindex == 98) or (rindex == 98) or (tindex == 0) or (rindex == 0):
            continue

        for t in reversed(row[:tindex]):
            left += 1
            if t >= tree:
                break
        for t in row[tindex + 1:]:
            right += 1
            if t >= tree:
                break
        for t in reversed([r[tindex] for r in trees][:rindex]):
            top += 1
            if t >= tree:
                break
        for t in [r[tindex] for r in trees][rindex + 1:]:
            bottom += 1
            if t >= tree:
                break

        scenic_score = left * right * top * bottom
        if scenic_score > max_scenic_score:
            max_scenic_score = max(max_scenic_score, scenic_score)
            max_scenic_score_coords = (rindex, tindex, left, right, top, bottom)
            rerow = list(reversed(row[:tindex]))
            ter = tree

print(max_scenic_score)
# print(max_scenic_score_coords)
# print(rerow)
# print(ter)