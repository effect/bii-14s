#!/usr/bin/python

outdata = open("allvectors.out", "w")

def gen_bin(vector, position):
	if position < len(vector):
		for nextvalue in ["0", "1"]:
			vector[position] = nextvalue
			gen_bin(vector, position + 1)
	else:
		outdata.write("".join(vector) + "\n")

with open("allvectors.in", "r") as indata:
	n = int(indata.readline().strip())

gen_bin(["0"] * n, 0)
