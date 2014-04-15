#!/usr/bin/python
from __future__ import division

def neighbor(combination, n):
	# passing k explicitly is redundant as it can be inferred from remaining data
	k = len(combination)
	recombination = combination[:]
	# find rightmost element not at its maximum value
	for boundary, _ in reversed(list(enumerate(recombination))):
		if recombination[boundary] < n - (k - boundary - 1):
			break
		if not boundary:
			raise ValueError("Cannot go past last combination.")
	# increment found element, fill the suffix with closest values
	recombination[boundary] += 1
	for index in xrange(boundary + 1, k):
		recombination[index] = recombination[index-1] + 1
	return recombination

with open("nextchoose.in", "r") as infile:
	[n, _]      = [int(x) for x in infile.readline().split()]
	combination = [int(x) for x in infile.readline().split()]

try:
	successor = neighbor(combination, n)
except:
	successor = ["-1"]

with open("nextchoose.out", "w") as outfile:
	outfile.write(" ".join(str(x) for x in successor))
