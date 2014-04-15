#!/usr/bin/python
from __future__ import division

def neighbor(permutation, backwards = False):
	# find boundary of longest descending/ascending suffix
	# (ascending for backwards neighbor, descending for forwards)
	for boundary, _ in reversed(list(enumerate(permutation))):
		if not boundary:
			raise ValueError("Cannot go past ultimate permutation.")
		boundaryOfAscending = backwards and (permutation[boundary - 1] > permutation[boundary])
		boundaryOfDescending = (not backwards) and (permutation[boundary - 1] < permutation[boundary])
		if boundaryOfAscending or boundaryOfDescending:
			break
	pivot = boundary - 1
	prefix = permutation[:pivot]
	suffix = sorted(permutation[pivot:], reverse = backwards)
	# find rightmost predecessor/successor to pivot value in the suffix
	# (predecessor for backwards neighbor, successor for forwards)
	for index, _ in enumerate(suffix):
		foundPredecessor = backwards and (suffix[index] < permutation[pivot])
		foundSuccessor = (not backwards) and (suffix[index] > permutation[pivot])
		if foundPredecessor or foundSuccessor:
			# swap pivot with predecessor/successor
			pivotvalue = suffix.pop(index)
			return prefix + [pivotvalue] + suffix

def neighborWithFallback(**kwargs):
	try:
		return neighbor(**kwargs)
	except:
		return [0] * len(kwargs["permutation"])

with open("nextperm.in", "r") as infile:
	initial = [int(x) for x in infile.readlines()[1].split()]

previousNeighbor = neighborWithFallback(
	permutation = initial,
	backwards = True
)
nextNeighbor = neighborWithFallback(
	permutation = initial
)

with open("nextperm.out", "w") as outfile:
	outfile.write(" ".join(str(x) for x in previousNeighbor) + "\n")
	outfile.write(" ".join(str(x) for x in nextNeighbor))
