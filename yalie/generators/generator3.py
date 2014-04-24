def gen_perm(a, p):
	if p < n:
		for i in range(1, n+1):
			if i not in a:
				a[p] = i
				gen_perm(a, p+1)
				a[p] = 0
	else:
		out.write(str(' '.join((str(i) for i in a)))+'\n')

infile = open('permutations.in', 'r')
n = int(infile.readline().strip())
infile.close()

out = open('permutations.out', 'w')
gen_perm([0 for i in range(n)], 0)
out.close()