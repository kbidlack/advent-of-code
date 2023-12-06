with open("input.txt", "r") as file:
    lines = file.readlines()

times = [int(num) for num in lines[0].strip().split(":")[1].split(" ") if num]
distances = [int(num) for num in lines[1].strip().split(":")[1].split(" ") if num]
races = dict(zip(times, distances))

ways = 0
waysum = []
for time, distance in races.items():
    ways = 0
    for i in range(time):
        d = i * (time - i)
        if d > distance:
            ways += 1
    waysum.append(ways)

print(waysum[0] * waysum[1] * waysum[2] * waysum[3])
