from operator import itemgetter


def bar(a, p, i):
    if i < n:
        a[i] = ''
        bar(a, p[1:], i + 1)

        for x in p:
            if x not in a:
                a[i] = x
                bar(a, p[1:], i + 1)

    else:
        answer.append([x for x in a])

with open('subsets.in', 'r') as infile:
    n = int(infile.readline().strip())

with open('subsets.out', 'w') as outfile:
    a = [0 for x in range(n)]
    p = [x for x in range(1, n + 1)]

    answer = []
    bar(a, p, 0)
    answer = [filter(None, x) for x in answer]
    for x in sorted(answer):
        outfile.write(' '.join([str(z) for z in x]) + '\n')
