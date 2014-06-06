#!/usr/bin/python
from __future__ import division

with open("airplane.in") as airplane_in:
	M, _, alpha = [int(x) for x in airplane_in.readline().split()]
	passenger_mass = sum(int(x) for x in airplane_in.readline().split())

try:
	result = (M + passenger_mass) * alpha / (1000 - alpha)
except ZeroDivisionError:
	result = "Impossible"

with open("airplane.out", "w") as airplane_out:
	airplane_out.write(str(result))
