input = open('./input.txt')
lines = input.readlines()

total = 0
scores = {'X': 1, 'Y': 2, 'Z': 3}

wins = {'C':'X', 'A':'Y', 'B':'Z'}
draws = {'A':'X', 'B':'Y', 'C':'Z'}
losses = {'B':'X', 'C':'Y', 'A':'Z'}

for line in lines:
    move = line[0]
    action = line[2]

    if action == 'X': # lose
        play = losses[move]
        win = 0
    elif action == 'Y': # draw
        play = draws[move]
        win = 3
    elif action == 'Z': # win
        play = wins[move]
        win = 6
    score = scores[play] + win
    total += score

print(total)
