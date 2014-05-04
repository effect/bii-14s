from collections import defaultdict


def bfs():
    ks = defaultdict(int)
    ks[1] = 0
    que = [1]
    while len(que) != 0:
        for x in g[que[0]]:
            if x not in ks:
                ks[x] = ks[que[0]] + 1
                que.append(x)
        del que[0]
    return(' '.join([str(x) for x in ks.values()]))

with open('pathbge1.in', 'r') as infile:

    g = defaultdict(list)
    edges = []

    n, m = [int(x) for x in infile.readline().strip().split()]

    for x in range(m):
        e = infile.readline().strip().split()
        if e[0] != e[1]:
            edges.append(e)

    for x, y in edges:
        g[int(x)].append(int(y))
        g[int(y)].append(int(x))


with open('pathbge1.out', 'w') as outfile:
    outfile.write(str(bfs()))
