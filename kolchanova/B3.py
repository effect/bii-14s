infile = open ("permutations.in","r")
outfile = open ("permutations.out",'w')

n = int (infile.readline().strip())

def generate_permutations (seq, loc):
	if loc < len (seq):
		for i in range (1, n+1):
			if i not in seq:
				seq[loc] = i
				generate_permutations (seq, loc+1)
			seq[loc] = 0
	else:
		outfile.write(" ".join([str(i) for i in seq]) + "\n")

generate_permutations (["0"] * n, 0)
			


