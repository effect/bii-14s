#file reading
ingraph = open('pathsg.in', 'r')
s = [int(i) for i in ingraph.readline().split()]
n = s[0]
m = s[1]
smezhn = {} #dict of dicts like adjacency list, with weights
for j in range(m):
	x = [int(i) for i in ingraph.readline().split()]
	if x[0] not in smezhn:
		smezhn[x[0]] = {x[1]: x[2]}
	else:
		smezhn[x[0]][x[1]] = x[2]
ingraph.close()

#distance matrix
d = [[1e100 for i in range(n)] for i in range(n)]
for i in range(n):
	for j in range(n):
		if i == j:
			d[i][j] = 0
for key in smezhn:
	for kk in smezhn[key]:
		d[key-1][kk-1] = smezhn[key][kk]

def floyd(d): #Floyd algorithm
	for k in range(n):
		for i in range(n):
			for j in range(n):
				d[i][j] = min(d[i][j], (d[i][k]+d[k][j]))

floyd(d)

out = open('pathsg.out', 'w')
for l in d:
	out.write(' '.join(str(i) for i in l))
	out.write('\n')
out.close()