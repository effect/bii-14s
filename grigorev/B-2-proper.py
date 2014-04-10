#!/usr/bin/python

def generator(subsequence, symbols, length):
	if len(subsequence) < length:
		for symbol in symbols:
			if symbol == "1" and len(subsequence) > 0 and subsequence[-1] == "1":
				continue
			for sequence in generator(subsequence + [symbol], symbols, length):
				yield sequence
	else:
		yield subsequence

with open("vectors.in", "r") as infile:
	n = int(infile.readline().strip())

with open("vectors.out", "w") as outfile:
	sequences = list(generator(
		subsequence = [],
		symbols     = ["0", "1"],
		length      = n
	))
	outfile.write(str(len(sequences)) + "\n")
	for sequence in sequences:
		outfile.write("".join(sequence) + "\n")
