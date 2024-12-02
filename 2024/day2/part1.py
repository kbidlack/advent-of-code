with open("input.txt", "r") as file:
    lines = file.readlines()

s = 0
for line in lines:
    ns = [int(x) for x in line.split(" ")]
    if list(sorted(ns)) == ns or list(sorted(ns, reverse=True)) == ns:
        for i, n in enumerate(ns):
            if i + 1 == len(ns):
                s += 1
                break
            if abs(ns[i + 1] - n) < 1 or abs(ns[i + 1] - n) > 3:
                break
        else:
            print(ns)
            s += 1


print(s)
