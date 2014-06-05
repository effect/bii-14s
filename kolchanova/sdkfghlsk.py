#!/usr/bin/python
infile = open ('harddrive.in','r')
_  = int(infile.readline())
parts = [int(x) for x in infile.readline().split()]

def function (parts):
	turns = -1
	backturn = set()

	for part in parts:
			if (part - 1) not in backturn:
				turns += 1
			backturn.add(part)
	return turns

result = function(parts)
#print result 
infile.close()
with open('harddrive.out', 'w') as outfile:
	outfile.write(str(result))