#WA in test 10, but this code is working!

def gen_subs(a):
	ans = []
	for i in range(2**n):
		tmp = []
		for j in range(n):
			if i & (1 << j):
				tmp.append(mn[j])
		ans.append(' '.join(str(i) for i in tmp))
	return ans


with open('subsets.in', 'r') as infile:
	n = int(infile.readline().strip())

mn = range(1, n+1)
subs = gen_subs(mn)
subs.sort()

with open('subsets.out', 'w') as out:
	out.write('\n'.join(subs))

print '\n'.join(subs)