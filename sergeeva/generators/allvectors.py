infile = open('allvectors.in', 'r')
outfile = open('allvectors.out', 'w')
n = int(infile.readline().strip())
 
a=[0]*n
def gen_bin(a,p):
    if p < n:
        a[p] = 0
        gen_bin(a, p+1)
        a[p] = 1
        gen_bin(a, p+1)
    else:
        outfile.write(str(''.join([str(i) for i in a])) + '\n')
gen_bin(a,0)
infile.close()
outfile.close()