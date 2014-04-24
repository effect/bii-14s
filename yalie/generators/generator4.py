def gen_comb(a, p):
	if p < k:
		for i in range(1, n+1):
			if i not in a and i > a[p-1]:
				a[p] = i
				gen_comb(a, p+1)
				a[p] = 0
	else:
		out.write(str(' '.join((str(i) for i in a)))+'\n')

infile = open('choose.in', 'r')
n, k = [int(i) for i in infile.readline().strip().split()]
infile.close()

out = open('choose.out', 'w')
gen_comb([0 for i in range(k)], 0)
out.close()