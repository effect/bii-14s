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
	# step-through like a digital clock (RTL)
	for pos, val in reversed(list(enumerate(vector))):
		if val == P:
			result[pos] = N
			return result
		else:
			result[pos] = P
	# fallback
	return ["-"]

with open("nextvector.in", "r") as infile:
	string = infile.readline().strip()
	vector = list(string)

predecessor = neighbor(vector, -1)
successor   = neighbor(vector, 1)

with open("nextvector.out", "w") as outfile:
	outfile.write("".join(predecessor) + "\n")
	outfile.write("".join(successor)   + "\n")
