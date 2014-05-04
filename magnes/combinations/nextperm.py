
def right(x):
    p = [int(i) for i in x[::-1]]

    i = 1
    while i < n and p[i - 1] < p[i]:
        i += 1

    if n == i:
        return ' '.join(['0' for x in range(n)])

    j = p.index(min([x for x in p[:i] if x > p[i]]))
    p[i], p[j] = p[j], p[i]
    p = p[:i][::-1] + p[i:]

    return ' '.join(list([str(i) for i in p[::-1]]))


def left(x):
    p = [int(i) for i in x[::-1]]

    i = 1
    while i < n and p[i - 1] > p[i]:
        i += 1

    if n == i:
        return ' '.join(['0' for x in range(n)])

    j = p.index(max([x for x in p[:i] if x < p[i]]))
    p[i], p[j] = p[j], p[i]
    p = p[:i][::-1] + p[i:]

    return ' '.join(list([str(i) for i in p[::-1]]))


with open('nextperm.in', 'r') as infile:

    n = int(infile.readline().strip())
    p = infile.readline().strip().split(' ')

with open('nextperm.out', 'w') as outfile:
    outfile.write(left(p) + '\n' + right(p))
