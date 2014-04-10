#!/usr/bin/python

with open("allvectors.in", "r") as infile:
	n = int(infile.readline().strip())

with open("allvectors.out", "w") as outfile:
	for x in xrange(2**n):
		s = bin(x).split("b")[1]
		outfile.write("0" * (n-len(s)) + s + "\n")
