#!/usr/bin/python
from __future__ import division

with open("harddrive.in") as infile:
	fragments = [
		int(x) for x in
		infile.readlines()[1].split()
	]

spins = -1
leftside = set()

for fragment in fragments:
	if (fragment - 1) not in leftside:
		spins += 1
	leftside.add(fragment)

with open("harddrive.out", "w") as outfile:
	outfile.write(str(spins))
