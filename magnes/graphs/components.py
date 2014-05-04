from collections import defaultdict


def bfs():
    num_ks = 0
    ks = {}
    for x in range(1, n + 1):
        if x not in ks:
            num_ks += 1
            ks[x] = num_ks
            que = [x]
            while len(que) != 0:
                for x in g[que[0]]:
                    if x not in ks:
                        ks[x] = num_ks
                        que.append(x)
                del que[0]
    return str(num_ks) + '\n' + ' '.join([str(x) for x in ks.values()])

with open('components.in', 'r') as infile:

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


with open('components.out', 'w') as outfile:
    outfile.write(dfs())
