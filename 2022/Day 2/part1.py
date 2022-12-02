input = open('./input.txt')
lines = input.readlines()

total = 0
scores = {'X': 1, 'Y': 2, 'Z': 3}

wins = [['X', 'C'], ['Y', 'A'], ['Z', 'B']]
draws = [['X', 'A'], ['Y', 'B'], ['Z', 'C']]
losses = [['X', 'B'], ['Y', 'C'], ['Z', 'A']]

for line in lines:
    move = line[0]
    play = line[2]

    if [play, move] in wins:
        win = 6
    if [play, move] in draws:
        win = 3
    if [play, move] in losses:
        win = 0

    score = scores[play] + win
    total += score

print(total)
