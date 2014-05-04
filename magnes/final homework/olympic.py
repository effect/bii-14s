from collections import defaultdict

with open('olympic.in', 'r') as infile:

    n = int(infile.readline().strip())

    data = []
    for x in infile:
        data.append(x.strip().split())

    prizes = defaultdict(lambda: defaultdict(lambda: 0))

    for a, b, c in data:
        prizes[a][0] += 1
        prizes[b][1] += 1
        prizes[c][2] += 1

    data = defaultdict(list)
    for x in prizes.items():
        for z in range(3):
            data[x[0]].append((x[1][z]))

    for i in range(3):
        out = []
        best = max([x[1][i] for x in data.items()])
        for x in data.items():
            if x[1][i] < best:
                out.append(x[0])
        for x in out:
            del data[x]

    data = [x for x in data]


with open('olympic.out', 'w') as outfile:
    outfile.write((sorted(data)[0]))
