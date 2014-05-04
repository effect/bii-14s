from collections import defaultdict

with open('tower.in', 'r') as infile:

    n = int(infile.readline().strip())
    data = []
    for x in infile:
        data.append(set([int(z) for z in x.strip().split()[1:]]))

    g = defaultdict(set)
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i] & data[j] and i != j:
                g[i].add(j)
                g[j].add(i)

    seen = set()
    que = [0]

    while que:
        for x in que:
            seen.add(x)
            for y in g[que[0]]:
                seen.add(y)
                que.extend([z for z in g[y] if z not in que and z not in seen])
            del que[0]


with open('tower.out', 'w') as outfile:
    outfile.write(str(len(seen)))
