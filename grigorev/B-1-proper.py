#!/usr/bin/python

def generator(subsequence, symbols, length):
	if len(subsequence) < length:
		for symbol in symbols:
			for sequence in generator(subsequence + [symbol], symbols, length):
				yield sequence
	else:
		yield subsequence

with open("allvectors.in", "r") as infile:
	n = int(infile.readline().strip())

with open("allvectors.out", "w") as outfile:
	sequences = generator(
		subsequence = [],
		symbols     = ["0", "1"],
		length      = n
	)
	for sequence in sequences:
		outfile.write("".join(sequence) + "\n")