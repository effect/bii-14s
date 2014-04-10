import re
infile = open('vectors.in', 'r')
outfile = open('vectors.out', 'w')

n = int(infile.readline().strip())

a = [0]*n
all_bin=[]
def gen_bin(a,p):
	if p < n:
		a[p] = 0
		gen_bin(a, p+1)
		a[p] = 1
		gen_bin(a, p+1)
	else:
		all_bin.append(str(''.join([str(i) for i in a])))
				
gen_bin(a,0)

ones=[]
for i in all_bin:
	for match in re.findall('11', i):
		ones.append(i)
ans=sorted(list(set(all_bin).difference(set(ones))))

outfile.write(str(len(ans))+'\n')
outfile.write(str('\n'.join([str(i) for i in ans])))
infile.close()
outfile.close()