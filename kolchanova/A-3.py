import sys 
sys.setrecursionlimit(100000)
#from collections import deque


infile = open('pathmgep.in', 'r')
outfile = open('pathmgep.out', 'w')

dimensions = [int(i) for i in infile.readline().split()]
n_vertices = dimensions[0] 
start = dimensions[1] 
end = dimensions[2] 

scope = [] 
def get_matrix (scope, infile, n_vertices):
    for i in range(n_vertices):
        y = [int(i) for i in infile.readline().split()]
        scope.append(y)
    return scope
get_matrix (scope, infile, n_vertices)


 
distances = {} #distance dict
def get_dist (distances, n_vertices):
    for i in range(1, n_vertices+1):
        distances[i] = -1
    return distances
get_dist (distances, n_vertices)


#the main algorithm
vertices = [] 
def dijkstra_alg (distances,start,end): 

    distances[start] = 0
    for y in range(n_vertices-1):

        vertices.append(start)
        for i in range(n_vertices):

            if scope[start-1][i] != -1:
                if distances[i+1] != -1:
                    distances[i+1] = min(distances[i+1], (distances[start]+scope[start-1][i]))
                else:
                    distances[i+1] = scope[start-1][i]+distances[start]
        assist = {} 
        for key in distances:
            if key not in vertices and distances[key] != -1:
                assist[key] = distances[key]
        if len(assist) == 0:
            break
        start = min(assist, key=lambda k: assist[k])
    return distances
dijkstra_alg (distances,start,end)
 
outfile.write(str(distances[end]))

infile.close()
outfile.close()