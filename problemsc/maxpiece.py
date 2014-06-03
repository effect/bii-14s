__author__ = 'Антон Брагин'

import itertools

def get_max_square_chop(xchops, ychops):
    xchops.sort(reverse=True)
    ychops.sort(reverse=True)
    return min(xchops[0], ychops[0])

if __name__ == '__main__':
    with open('maxpiece.in') as f:
        n, m, k = [int(x) for x in f.readline().split()]
        xcuts = []
        ycuts = []
        for _ in range(k):
            axis, coord = [int(x) for x in f.readline().split()]
            if axis == 0:
                xcuts.append(coord)
            else:
                ycuts.append(coord)
    #Sort x and y chops
    xcuts.append(0)
    ycuts.append(0)
    xcuts.append(n)
    ycuts.append(m)
    xcuts.sort()
    ycuts.sort()

    xchops = []
    ychops = []
    for i in range(len(xcuts) - 1):
        xchops.append(xcuts[i + 1] - xcuts[i])
    for j in range(len(ycuts) - 1):
        ychops.append(ycuts[j + 1] - ycuts[j])

    max_square = get_max_square_chop(xchops, ychops)

    with open('maxpiece.out', 'w') as f:
        f.write(str(max_square))





