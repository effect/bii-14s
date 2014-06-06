import sys
from collections import defaultdict
sys.setrecursionlimit(200000)

from collections import deque
input_file = open('components.in', 'r')
output_file = open('components.out', 'w')

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

def search_df ():
	conn_comp = {}
	coconut = 0
	for i in vertices:
		if i not in conn_comp:
			coconut += 1
			conn_comp[i] = coconut
			queue = deque ([i])


			while len(queue) > 0:
				for j in adj[queue[0]]:
					if j not in conn_comp:
						conn_comp[j] = coconut
						queue.append (j)
				
				queue.popleft ()
	output_file.write(str(coconut)+"\n")
	for i in conn_comp.values ():
		output_file.write(str(i)+" ")
search_df()

input_file.close()
output_file.close ()



