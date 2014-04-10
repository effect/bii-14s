import sys
sys.setrecursionlimit(100000)


input_file = open('pathsg.in', 'r')
output_file = open('pathsg.out', 'w')

nodes, edges = [int(i) for i in input_file.readline().split()]
dist = []
#cumulative_w = 0
dist = [[None for i in range(nodes)] for j in range(nodes)]


def get_dist (dist,nodes):
	cumulative_w = 0 #?why here
	#for j in range (nodes):
		#dist[j][j] = 0
	
	#return dist

#get_dist (dist,nodes)

#def count_w (edges, input_file,dist,cumulative_w):
	for j in range (edges):
		#
			x,y,z = [int (w) for w in input_file.readline().split()]
			dist [x-1][y-1] = z
			cumulative_w += z
	#return dist
	#return cumulative_w

#count_w (edges, input_file,dist,cumulative_w)

#def secure (nodes, dist, cumulative_w):
	for j in range (nodes):
		for i in range (nodes):
			if j == i:
				dist[j][i] = 0
			elif dist[j][i] is None:
				dist [j][i] = cumulative_w +1 
	return dist

#secure (nodes, dist, cumulative_w)

def F_W (nodes, dist):
	for i in range (nodes):
		for j in range (nodes):
			for x in range (nodes):
				if dist[j][i] + dist[i][x] < dist [j][x]:
					dist [j][x] = dist [j][i] + dist [i][x]
				#dist [j][x] = min (dist [j][x], dist [j][i] + dist[i][x])
	return dist

get_dist (dist,nodes)
#count_w (edges, input_file,dist,cumulative_w)
#secure (nodes, dist, cumulative_w)
F_W (nodes,dist)

for line in dist:
	#for i in line:
	output_file.write(' '.join(str(i) for i in line) + '\n' )
   
#output_file.write('\n')
input_file.close()
output_file.close()
