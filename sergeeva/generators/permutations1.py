infile = open('permutations.in', 'r')
outfile = open('permutations.out', 'w')

n = int(infile.readline().strip())
seq=range(1,n+1)

ans=[]

def permutation(seq, i):
    if i == len(seq)-1:
        ans.append(str(''.join([str(i) for i in seq])))
    else:
        for j in range(i, len(seq)):
            seq[i], seq[j] = seq[j], seq[i]
            permutation(seq, i+1)
            seq[i], seq[j] = seq[j], seq[i] 
        
permutation(seq, 0)
for i in sorted(ans):
	outfile.write(str(' '.join([str(j) for j in i])+'\n'))
infile.close()
outfile.close()