from collections import deque
 
infile = open('components.in', 'r')
outfile = open('components.out', 'w')
 
n,e = [int(i) for i in infile.readline().split()] 
 
#edgelist
edges=[] 
for i in range(e):
    edges.append([int(j) for j in infile.readline().split()])
 
#neighbours
from collections import defaultdict
neighbours = defaultdict(lambda: defaultdict(lambda: 0))
for v1, v2 in edges:
    neighbours[v1][v2] += 1
    neighbours[v2][v1] += 1
 
def dfs():
    num_component ={}
    comp = 0
    for i in range(1, n+1):
        if i not in num_component:
            comp += 1
            num_component[i] = comp
            queue = deque([i])
            while len(queue) > 0:
                for v in neighbours[queue[0]]:
                    if v not in num_component:
                        num_component[v] = comp
                        queue.append(v)
                queue.popleft()
    outfile.write(str(comp)+ '\n')
    for i in num_component.values():
        outfile.write(str(i)+' ')
dfs()
 
 
infile.close()
outfile.close()