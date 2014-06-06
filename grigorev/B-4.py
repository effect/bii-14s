#!/usr/bin/python
from __future__ import division

def generator(subsequence, numbers, length):
	if len(subsequence) < length:
		for number in numbers:
			if number > max(subsequence + [-1]):
				for sequence in generator(subsequence + [number], numbers, length):
					yield sequence
	else:
		yield subsequence

with open("choose.in", "r") as infile:
	n, k = [int(x) for x in infile.readline().split()]

choices = generator(
	subsequence = [],
	numbers = list(range(1, n+1)),
	length = k
)

with open("choose.out", "w") as outfile:
	for choice in choices:
		outfile.write(" ".join(str(x) for x in choice) + "\n")
