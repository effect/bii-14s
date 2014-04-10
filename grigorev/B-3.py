#!/usr/bin/python
from __future__ import division

def generator(subsequence, symbols):
	complete = True
	for symbol in symbols:
		if symbol not in subsequence:
			complete = False
			for sequence in generator(subsequence + [symbol], symbols):
				yield sequence
	if complete:
		yield subsequence

with open("permutations.in", "r") as infile:
	n = int(infile.readline().strip())

permutations = generator(
	subsequence = [],
	symbols = [str(x) for x in xrange(1, n + 1)]
)

with open("permutations.out", "w") as outfile:
	for permutation in permutations:
		outfile.write(" ".join([str(x) for x in permutation]) + "\n")
