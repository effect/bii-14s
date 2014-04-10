#!/usr/bin/python

with open("vectors.in", "r") as infile:
	n = int(infile.readline().strip())

vectors = [
	bin(x).split("b")[1]
	for x in xrange(2**n)
	if bin(x).count("11") == 0
]

with open("vectors.out", "w") as outfile:
	outfile.write(str(len(vectors)) + "\n")
	for vector in vectors:
		outfile.write("0" * (n - len(vector)) + vector + "\n")
