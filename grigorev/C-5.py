#!/usr/bin/python

def piece_sizes(cuts):
	sorted_cuts = sorted(cuts)
	return [
		sorted_cuts[i] - sorted_cuts[i-1]
		for i in range(1, len(sorted_cuts))
	]

with open("maxpiece.in") as infile:
	lines = infile.readlines()

n, m, _ = [int(x) for x in lines[0].split()]
cuts_x = [0, n]
cuts_y = [0, m]

for line in lines[1:]:
	t, v = [int(x) for x in line.split()]
	if t == 0:
		cuts_x.append(v)
	else:
		cuts_y.append(v)

biggest_square = min(
	max(piece_sizes(cuts_x)),
	max(piece_sizes(cuts_y))
)

with open("maxpiece.out", "w") as outfile:
	outfile.write(str(biggest_square))
