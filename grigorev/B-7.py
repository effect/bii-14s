#!/usr/bin/python
from __future__ import division

def descending(vector):
	return (sorted(vector)[::-1] == vector)

def ascending(vector):
	return (sorted(vector) == vector)

def successor(vector):
	if descending(vector):
		return [0] * len(vector)
	if len(vector) == 2:
		return vector[::-1]
	head = vector[0]
	tail = vector[1:]
	if descending(tail):
		tail = sorted(vector)
		head = tail.pop(tail.index(head) + 1)
		return [head] + tail
	return [head] + successor(tail)

def predecessor(vector):
	if ascending(vector):
		return [0] * len(vector)
	if len(vector) == 2:
		return vector[::-1]
	head = vector[0]
	tail = vector[1:]
	if ascending(tail):
		tail = sorted(vector)[::-1]
		head = tail.pop(tail.index(head) + 1)
		return [head] + tail
	return [head] + predecessor(tail)

with open("nextperm.in", "r") as infile:
	vector = [int(x) for x in infile.readlines()[1].split()]

P = predecessor(vector)
S = successor(vector)

with open("nextperm.out", "w") as outfile:
	outfile.write(" ".join([str(x) for x in P]) + "\n")
	outfile.write(" ".join([str(x) for x in S]) + "\n")
