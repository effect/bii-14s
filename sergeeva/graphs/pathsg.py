#floyd 
infile = open('pathsg.in', 'r')
outfile = open('pathsg.out', 'w')
 
n,e = [int(i) for i in infile.readline().split()] 
 
dist = [[float('inf') for i in range(n)] for j in range(n)]
 
sum=0
for i in range(e):
    u, v, weight = [int(x) for x in infile.readline().split()]
    dist[u-1][v-1] = weight
    sum += weight
 
for i in range(n):
    for j in range(n):
        if i == j:
            dist[i][j] = 0
        elif dist[i][j] == float('inf'):
            dist[i][j] = sum +1
 
def floyd(dist): 
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], (dist[i][k] + dist[k][j]))
  
floyd(dist)
 
for row in dist:
    outfile.write(' '.join(str(i) for i in row) + '\n')
infile.close()
outfile.close()