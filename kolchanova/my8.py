#!/usr/bin/python

with open('nextchoose.in') as infile:
    number, n = [int(x) for x in infile.readline().split()]
    combination = [int(x) for x in infile.readline().split()]

def mk_choice(number, n, combination):
    for x in range(n):
        if combination [ n - x - 1 ] < number - x:
            combination [ n - x -1 ] += 1
            for y in range ( n - x, n ):
                combination [y] = combination [ y - 1 ] + 1
            return combination
    return [-1]

result = mk_choice (number, n, combination)
#print result
with open ('nextchoose.out', 'w') as outfile:
	outfile.write(" ".join(str(x) for x in result)) 