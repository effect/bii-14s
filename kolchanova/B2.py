#!/usr/bin/python

indata = open ("vectors.in","r")
outdata = open ("vectors.out",'w')

n = int (indata.readline().strip())
vectors = []

def gener_vect (vector, position):
    if position < len (vector):
        for next in ["0","1"]:
            if position > 0 and next  == "1" and vector[position-1] == "1":
                pass
            else:
                vector[position] = next
                gener_vect(vector, position + 1)
    else :
        vectors.append (vector[:])
    return vectors


gener_vect (["0"] * n, 0)

outdata.write (str(len(vectors))+"\n")
for vector in vectors:
    outdata.write("".join(vector) + "\n")