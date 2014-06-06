#!/usr/bin/python

with open("maxpiece.in") as infile:
        n, m, k = [int(x) for x in infile.readline().split()]
        xcuts = [0, n]
        ycuts = [0, m]
        for line in infile:
                t, v = [int(x) for x in line.split()]
                if t == 0:
                        xcuts.append(v)
                else:
                        ycuts.append(v)

xcuts.sort()
xsizes = []
for i, _ in enumerate(xcuts):
        if i > 0:
                xsizes.append(xcuts[i] - xcuts[i-1])

ycuts.sort()
ysizes = []
for i, _ in enumerate(ycuts):
        if i > 0:
                ysizes.append(ycuts[i] - ycuts[i-1])

biggest_square = min(max(xsizes), max(ysizes))

with open("maxpiece.out", "w") as outfile:
        outfile.write(str(biggest_square))