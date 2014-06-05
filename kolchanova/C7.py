#!/usr/bin/python
from __future__ import division

with open("airplane.in") as infile:
	M, N, alpha = [int(x) for x in infile.readline().split()]
	passenger_mass = sum(int(x) for x in infile.readline().split())

mass_on_empty = M + passenger_mass

if alpha == 1000:
	result = "Impossible"
else:
	result = mass_on_empty * alpha / (1000 - alpha)

with open("airplane.out", "w") as outfile:
	outfile.write(str(result))