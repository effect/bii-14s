#reading a file
ingraph = open('spantree.in','r')
n = int(ingraph.readline().strip())
p = [] #a list of lists with all points
for i in range(n):
	t = [int(i) for i in ingraph.readline().split()]
	p.append(t)
ingraph.close()

#calculation of length of the edge
def le(a,b):
	import math
	m = math.sqrt((p[a][0] - p[b][0])**2 + (p[a][1] - p[b][1])**2)
	return m

#saving a graph to the matrix
def sm(p):
	smezhn = [['x' for i in range(n)] for j in range(n)]
	for i in range(n):
		for j in range(n):
			smezhn[i][j] = le(i,j)
	return smezhn

#Prim algorithm
def Prim(smezhn):
	used = []
	mine = []
	for i in range(n):
		used.append(False)
		mine.append('x')
	used[0] = True
	mine[0] = 0
	idx = 0
	for i in range(n-1):
		tmp = {}
		for j in range(n):
			if not used[j]:
				mine[j] = min(mine[j], smezhn[idx][j])
				tmp[j] = mine[j]
		idx = min(tmp, key=tmp.get) #finding an index (node) of edge with min weight
		used[idx] = True
	return mine

smezhn = sm(p)
wedge = Prim(smezhn)
ans = sum(wedge)

out = open('spantree.out', 'w')
out.write(str(ans))
out.close()