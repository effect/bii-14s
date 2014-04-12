def gen_bin(p, a):
	if p < n:
		a[p] = 0
		gen_bin(p+1, a)
		a[p] = 1
		gen_bin(p+1, a)
	else:
		v = ''.join(str(i) for i in a)
		if '11' not in v:
			global not11 
			not11 += 1
			tmp[not11-1] = str(v)
	return not11
		
inf = open('vectors.in')
n = int(inf.readline().strip())
inf.close()

not11 = 0
tmp = [0 for i in range(2**n)]
ansver = gen_bin(0, [0 for i in range(n)])

out = open('vectors.out', 'w')
out.write(str(ansver) + '\n')
for i in tmp:
	if i != 0:
		out.write(str(i) + '\n')
out.close()