with open("input.txt", "r") as file:
    lines = file.readlines()

ss = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

houses = [list() for _ in range(7)]
for index, line in enumerate(lines):
    card = line.split(" ")[0]
    if any(card.count(s) == 5 for s in ss):  # five of a kind
        houses[0].append(card)
    elif any(card.count(s) == 4 for s in ss):
        houses[1].append(card)
    elif any(card.count(s) == 3 for s in ss):
        if any(card.count(s) == 2 for s in ss):
            houses[2].append(card)
        else:
            houses[3].append(card)
    elif any(card.count(s) == 2 for s in ss):
        if [card.count(s) for s in ss].count(2) == 2:
            houses[4].append(card)
        else:
            houses[5].append(card)
    else:
        houses[6].append(card)
from string import ascii_letters

ordered_cards = []
for house in houses:
    shouse = ["".join([ascii_letters[ss.index(c)] for c in card]) for card in house]
    shouse.sort()
    ordered_cards.extend(
        ["".join([ss[ascii_letters.index(c)] for c in card]) for card in shouse]
    )

winnings = []

for i, c in enumerate(reversed(ordered_cards)):
    rank = i + 1
    bid = int(next(line for line in lines if c in line).split(" ")[1].strip())
    # print(c, bid, rank)
    winnings.append(rank * bid)

total = sum(winnings)
print(total)
