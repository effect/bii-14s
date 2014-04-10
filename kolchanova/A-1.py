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




#graph = {}

#for z in edges:
#	x = [int(i) for i in input_file.readline().split()]
#	if x[0] in graph:
#		graph[x[0].append(x[1])]
	#elif x [1] in adjacent:
		#adjacent[x[1]].append(x[0])
#	else:
#		graph[x[0]] = [x[1]]
#	if x [1] in graph:
#		graph[x[1]].append(x[0])
#	else: 
#		graph [x[1]] = x [0]
#for w in vertices:
#	if w not in graph:
#		graph[w] = []

####### QUATSCH #####
###def funct (x,y):


#from collections import defaultdict
#der_graph = defaultdict(list)


##der_graph = {}
#for x in vertices:
#	funct (x,y)


#	if start in der_graph:
	#for j in range (int(i), int (i+2):
#	der_graph[x].append(end)
#	else: der_graph[start] = [end]
	#x+=1
#print der_graph
###### QUATSCH ENDET HIER ##### 

#conn_comp = {}
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
	#return conn_comp
	output_file.write(str(coconut)+"\n")
	for i in conn_comp.values ():
		output_file.write(str(i)+" ")
search_df()

input_file.close()
output_file.close ()

#search_df()

#answer  = conn_comp.values ()
#for i in answer:
#	output_file.write(str(i) + " ")

#input_file.close ()
#output_file.close ()


