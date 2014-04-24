def gen_subs(line, l):
	ans.append(' '.join(str(i) for i in line))
	for i in mn:
		if i > l:
			gen_subs(line + [i], i)
	return ans

with open('subsets.in', 'r') as infile:
	n = int(infile.readline().strip())

mn = range(1, n+1)
ans = []
gen_subs([], 0)

with open('subsets.out', 'w') as out:
	out.write('\n'.join(ans))