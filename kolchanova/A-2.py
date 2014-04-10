import sys
sys.setrecursionlimit(200000)

from collections import deque
from collections import defaultdict
input_file = open('pathbge1.in', 'r')
output_file = open('pathbge1.out', 'w')


def function():
	pass

#[vert,edg] = [int(x) for x in input_file.readline().split()]
#graph_korp = {vert : [] for ver in xrange (1, vert+1)}
#alllengths = 1
#for info in input_file.readline().split():
#		[start,end] = [int(x) for x in info.split()]
#		graph_korp[start].append(end)
#		graph_korp[end].append(start)
	#def
	#return graph_korp


n_vertices, n_edges = [int(i) for i in input_file.readline().split()]
vertices = []
edges = []
for i in range(1, n_vertices+1):
	vertices.append (i)
	#vertices.pop [0]
	i += 1
for j in range (n_edges):
	edges.append ([int(j) for j in input_file.readline().split()])
	#j+=1

#print vertices
#print edges

#start, end = [int (i) for i in input_file.readline().split()] 

adj = defaultdict (lambda: defaultdict(lambda: 0))

for x, y in edges:
	adj[x][y] += 1
	adj [y][x] += 1


#distances = {}
distances = {1:0}
def BFS ():
	#dist = {1:0}
	queue = deque ([1])
	while len (queue):
		for i in adj[queue[0]]:
			if i not in distances:
				distances[i] = distances[queue[0]] + 1
				queue.append(i)
		queue.popleft()
	return distances

BFS ()

answer = distances.values()
for i in answer:
	output_file.write(str(i)+ " ")
input_file.close ()
output_file.close ()


#n_vertices, n_edges = [int(i) for i in input_file.readline().split()]

#vertices = []
#edges = []
#for i in range(1, n_vertices+1):
#	vertices.append (i)
	#vertices.pop [0]
#	i += 1
#for j in range (1,n_edges+1):
#	edges.append (j)
#	j+=1

#the_graph = {}

#def merge (x,y):
#	if x not in the_graph:

