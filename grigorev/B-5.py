#!/usr/bin/python
from __future__ import division

def generator(subsequence, numbers):
	yield subsequence
	for number in numbers:
		if number > max(subsequence + [-1]):
			for sequence in generator(subsequence + [number], numbers):
				yield sequence

with open("subsets.in", "r") as infile:
	n = int(infile.readline().strip())

subsets = generator(
	subsequence = [],
	numbers = list(xrange(1, n+1))
)

with open("subsets.out", "w") as outfile:
	for subset in subsets:
		outfile.write(" ".join(str(x) for x in subset) + "\n")
