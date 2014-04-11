#!/usr/bin/python

infile = open ("choose.in",'r')
outfile = open ("choose.out",'w')

n, k = (int(x) for x in infile.readline().split())
variants = []

def gener_comb (combination, position, n):
	if position < k:
		for i in range (1, n+1):
			if i not in combination:
				if position > 0 and i < combination[position-1]:
					pass
				else:
					combination[position] = i
					gener_comb (combination, position+1, n)
			combination[position] = 0
	else:
		variants.append(combination[:])
	return variants
gener_comb ([0]*k, 0, n)

for v in variants:
	outfile.write(" ".join([str(x) for x in v]) + "\n")


