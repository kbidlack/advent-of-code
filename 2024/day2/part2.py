with open("input.txt", "r") as file:
    lines = file.readlines()


def safe(ns):
    if list(sorted(ns)) == ns or list(sorted(ns, reverse=True)) == ns:
        for i, n in enumerate(ns):
            if i + 1 == len(ns):
                return True
                break
            if abs(ns[i + 1] - n) < 1 or abs(ns[i + 1] - n) > 3:
                break
        else:
            print(ns)
            return True


s = 0
for line in lines:
    ns = [int(x) for x in line.split(" ")]
    if safe(ns):
        s += 1
    else:
        for i, _ in enumerate(ns):
            nn = ns.copy()
            nn.pop(i)
            if safe(nn):
                s += 1
                break


print(s)
