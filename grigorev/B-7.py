#!/usr/bin/python
from __future__ import division
from math import factorial, floor
from itertools import count

def factoradic(decimal, positions):
	if decimal < 0 or decimal != int(decimal):
		raise ValueError("Factoradic implemented only for positive integers.")
	digits = []
	for radix in count(start = 1):
		if decimal:
			digits.append(int(decimal % radix))
			decimal = floor(decimal / radix)
		else:
			break
	if len(digits) < positions:
		digits += [0] * (positions - len(digits))
	return digits[::-1]

def decimal(factoradic):
	return sum(
		digit * factorial(position)
		for position, digit
		in enumerate(reversed(factoradic))
	)

def encodeLehmer(permutation):
	lehmer = [0] * len(permutation)
	for i, _ in enumerate(permutation):
		for j, _ in list(enumerate(permutation))[i+1:]:
			if permutation[j] < permutation[i]:
				lehmer[i] += 1
	symbols = sorted(permutation)
	number  = decimal(lehmer)
	return symbols, number

def decodeLehmer(symbols, number):
	permutation = []
	symbolsSHC = symbols[:]
	try:
		code = factoradic(number, len(symbols))
		for digit in code:
			permutation.append(symbolsSHC.pop(digit))
	except:
		return ["0"] * len(symbols)
	return permutation

with open("nextperm.in", "r") as infile:
	permutation = infile.readlines()[1].split()

symbols, number = encodeLehmer(permutation)
predecessor     = decodeLehmer(symbols, number - 1)
successor       = decodeLehmer(symbols, number + 1)

with open("nextperm.out", "w") as outfile:
	outfile.write(" ".join(predecessor) + "\n")
	outfile.write(" ".join(successor))
