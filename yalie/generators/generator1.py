def gen_bin(p, a):
	if p < n:
		a[p] = 0
		gen_bin(p+1, a)
		a[p] = 1
		gen_bin(p+1, a)
	else:
		out.write(str(''.join((str(i) for i in a)))+'\n')
		
inf = open('allvectors.in')
n = int(inf.readline().strip())
inf.close()

out = open('allvectors.out', 'w')
gen_bin(0, [0 for i in range(n)])
out.close()