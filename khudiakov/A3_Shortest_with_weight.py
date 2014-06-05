
import sys
sys.setrecursionlimit(1000000000)
 
#read number of vertices, star and stop points from file
file = open('pathmgep.in', 'r')
 
n, s, f = [int(i) for i in file.readline().split()]
s-= 1
f-= 1
 
#read weight matrix
path = []
for string in file.read().splitlines():
    weight = [int(i) for i in string.split()]
    path.append(weight)
file.close()
 
#mark nonexistent paths
for i in range(n):
    for j in range(n):
        if path[i][j] == -1:
            path[i][j] = '-1'
 
#may be slow but..
def FloydWarshall(path):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if path[i][j] != '-1'and path[i][k] != '-1'and path[k][j] != '-1':
                      path[i][j] = min(path[i][j], (path[i][k] + path[k][j]))
                elif path[i][j] != '-1'and (path[i][k] == '-1'or path[k][j] == '-1'):
                    path[i][j] = path[i][j]
                elif path[i][j] == '-1'and path[i][k] != '-1'and path[k][j] != '-1':
                    path[i][j] = path[i][k] + path[k][j]
                else:
                    path[i][j] = '-1'
    return path
  
FloydWarshall(path)
 
 
ans = open('pathmgep.out', 'w')
ans.write(str(path[s][f]))
ans.close()