#!/usr/bin/python
from __future__ import division

def neighbor(vector, direction):
	# decide what symbols to consider (P)revious and (N)ext
	if direction == 1:
		P, N = ["0", "1"]
	else:
		P, N = ["1", "0"]
	# create a copy of vector
	result = vector[:]
	# step-through like a digital clock
	for pos, val in enumerate(vector):
		if val == P:
			result[pos] = N
			return result
		else:
			result[pos] = P
	# fallback
	return ["-"]

with open("nextvector.in", "r") as infile:
	string = infile.readline().strip()
	vector = list(string)[::-1] # we order positions RTL when interpreting binary

predecessor = neighbor(vector, -1)
successor   = neighbor(vector, 1)

with open("nextvector.out", "w") as outfile:
	# positional notation: reverse order again
	outfile.write("".join(predecessor[::-1]) + "\n")
	outfile.write("".join(successor[::-1])   + "\n")
