infile = open('pathbge1.in', 'r')
outfile = open('pathbge1.out', 'w')
  
n,e = [int(i) for i in infile.readline().split()] 
 
#edgelist
edges=[] 
for i in range(e):
    edges.append([int(j) for j in infile.readline().split()])
 
#linking edges
def link(u, v):
    if u not in graph:
        graph[u] = {}
    (graph[u])[v] = 1
    if v not in graph:
        graph[v] = {}
    (graph[v])[u] = 1
    return graph
 
graph = {}
for (x,y) in edges: 
    link(x,y)
dist = {} #distance

def bfs (s, v):
    q = [s] #queue
    dist[s] = 0
    while len(q) > 0:
        current = q.pop(0)
        for i in graph[current].keys():
            if i not in dist:
                dist[i] = dist[current] + 1
                if i == v:
                    return dist[v]
                q.append(i)
    return dist
 
bfs(1,n+1)
for j in dist.values():
    outfile.write(str(j) + ' ')
 
infile.close()
outfile.close()