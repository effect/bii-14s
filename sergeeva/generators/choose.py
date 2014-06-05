infile = open('choose.in', 'r')
outfile = open('choose.out', 'w')

n, k = [int(i) for i in infile.readline().split()]
seq=range(1,n+1)

def choose(seq, k):
    if k == 0:
        yield []
    else:
        for i, x in enumerate(seq):
            for c in choose(seq[i+1:], k-1):
                yield [x] +c

for i in choose(seq, k):
    outfile.write(str.join(' ', (str(j) for j in i)) + '\n')

infile.close()
outfile.close()

