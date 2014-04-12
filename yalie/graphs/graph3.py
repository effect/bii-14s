#file reading
ingraph = open('pathmgep.in', 'r')
x = [int(i) for i in ingraph.readline().split()]
N = x[0] #number of nodes
S = x[1] #start
F = x[2] #finish
msm = [] #incidence matrix
for i in range(N):
	y = [int(i) for i in ingraph.readline().split()]
	msm.append(y)
ingraph.close()

d = {} #distance dict
for i in range(1, N+1):
	d[i] = -1
n = [] #list of nodes

def Dejkstra(d,S,F): # Dejkstra algorithm
	d[S] = 0
	for y in range(N-1):
		n.append(S)
		for i in range(N):
			if msm[S-1][i] != -1:
				if d[i+1] != -1:
					d[i+1] = min(d[i+1], (d[S]+msm[S-1][i]))
				else:
					d[i+1] = msm[S-1][i]+d[S]
		a = {} #only help in finding a min node
		for key in d:
			if key not in n and d[key] != -1:
				a[key] = d[key]
		if len(a) == 0:
			break
		S = min(a, key=lambda k: a[k])
	return d

Dejkstra(d,S,F)

out = open('pathmgep.out', 'w')
out.write(str(d[F]))
out.close()

print d[F]