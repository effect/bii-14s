#!/usr/bin/python

def nextvector (seq):
	result = seq[:]
	for x,y in reversed(list(enumerate(seq))):
		if y == '0':
			result[x] = '1'
			return result
		else:
			result[x] = '0'
	return ['-']

def previousvector (seq):
	result = seq[:]
	for x,y in reversed(list(enumerate(seq))):
		if y == '1':
			result[x] = '0'
			return result
		else:
			result[x] = '1'
	return ['-']

with open ('nextvector.in', 'r') as infile:
	seq = list(infile.readline().strip())

preceding = previousvector(seq)
following = nextvector(seq)

with open ('nextvector.out', 'w') as outfile:
	outfile.write(''.join(preceding) + '\n')
	outfile.write(''.join(following) + '\n')
