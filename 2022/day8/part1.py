with open('input.txt', 'r') as file:
    lines = file.readlines()

trees: list[list] = []
total = 0

for line in lines:
    trees.append([int(char) for char in line if char != '\n'])

for rindex, row in enumerate(trees):
    for tindex, tree in enumerate(row):
        if tindex == 98:
            visible_from_left = None
            visible_from_right = True
            visible_from_top = None
            visible_from_bottom = None
        elif rindex == 98:
            visible_from_bottom = True
            visible_from_right = None
            visible_from_left = None
            visible_from_top = None
        else:
            visible_from_left = tree > max(row[:tindex], default=-1)
            visible_from_right = tree > max(row[tindex + 1:], default=-1)
            visible_from_top = tree > max([r[tindex] for r in trees[:rindex]], default=-1)
            visible_from_bottom = tree > max([r[tindex] for r in trees[rindex + 1:]], default=-1)
    
        visible = visible_from_left or visible_from_right or visible_from_bottom or visible_from_top
        if visible:
            total += 1

print(total)