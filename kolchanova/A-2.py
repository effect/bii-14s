import sys
sys.setrecursionlimit(200000)

from collections import deque
from collections import defaultdict
input_file = open('pathbge1.in', 'r')
output_file = open('pathbge1.out', 'w')


def function():
	pass


n_vertices, n_edges = [int(i) for i in input_file.readline().split()]
vertices = []
edges = []
for i in range(1, n_vertices+1):
	vertices.append (i)
	i += 1
for j in range (n_edges):
	edges.append ([int(j) for j in input_file.readline().split()])


adj = defaultdict (lambda: defaultdict(lambda: 0))

for x, y in edges:
	adj[x][y] += 1
	adj [y][x] += 1


distances = {1:0}
def BFS ():
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



