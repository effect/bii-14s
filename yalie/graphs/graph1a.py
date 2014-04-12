from collections import deque

#file reading
ingraph = open('components.in', 'r')
s = [int(i) for i in ingraph.readline().split()]
n = s[0]
m = s[1]
smezhn = {} #dict like adjacency list 
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

#depth-first search
comp = {} #dict of components
def dfs():
	cc = 0 #number of components
	for i in range(1, n+1):
		if i not in comp:
			cc += 1
			comp[i] = cc
			queue = deque([i])
			while len(queue) > 0:
				for j in smezhn[queue[0]]:
					if j not in comp:
						comp[j] = cc
						queue.append(j)
				queue.popleft()
	out = open('components.out', 'w')
	out.write(str(cc)+'\n')
	out.close()

dfs()

#saving results
out = open('components.out', 'a')
a = comp.values()
for k in a:
	out.write(str(k)+' ')
out.close()