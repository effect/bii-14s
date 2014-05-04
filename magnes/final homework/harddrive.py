from collections import defaultdict

with open('harddrive.in', 'r') as infile:
    n = int(infile.readline().strip())
    data = [int(x) for x in infile.readline().strip().split()]

    starts = defaultdict(int)

    for x in data:
        if x - 1 not in starts:
            starts[x] = 1
        if x - 1 in starts:
            starts[x - 1] = 0
            starts[x] = 1

with open('harddrive.out', 'w') as outfile:
    outfile.write(str(len([x for x in starts if starts[x]]) - 1))
