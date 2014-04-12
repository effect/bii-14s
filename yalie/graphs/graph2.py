from collections import deque

smezhn = {} #dict like adjacency list 
dist = {} #a dict of distances
dist[1] = 0

def read(): #file reading
	ingraph = open('pathbge1.in', 'r')
	s = [int(i) for i in ingraph.readline().split()]
	n = s[0]
	m = s[1]
	for j in range(m):
		x = [int(i) for i in ingraph.readline().split()]
		if x[0] in smezhn:
			smezhn[x[0]].append(x[1])
		else:
			smezhn[x[0]] = [x[1]]
		if x[1] in smezhn: #because here is not-directed graph
			smezhn[x[1]].append(x[0])
		else:
			smezhn[x[1]] = [x[0]]
	for i in range(1, n+1):
		if i not in smezhn:
			smezhn[i] = []
	ingraph.close()
	return smezhn

def bfs():
	queue = deque([1])
	while len(queue) > 0:
		for i in smezhn[queue[0]]:
			if i not in dist:
				dist[i] = dist[queue[0]] + 1
				queue.append(i)
		queue.popleft()
	return dist

read()
bfs()
out = open('pathbge1.out', 'w')
a = dist.values()
for k in a:
	out.write(str(k)+' ')
out.close()