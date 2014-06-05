infile = open('pathmgep.in', 'r')
outfile = open('pathmgep.out', 'w')
 
n, S, F = [int(i) for i in infile.readline().split()] 

dist = []

sum=0
for line in infile.read().splitlines():
    values = [int(i) for i in line.split()]
    dist.append(values)
    for i in values:
    	if i>0:
    		sum+=i

for i in range(n):
    for j in range(n):
       	if dist[i][j] == -1:
       		dist[i][j] = sum +1

def floyd(dist): 
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], (dist[i][k] + dist[k][j]))


floyd(dist)

if dist[S-1][F-1]>=sum:
	dist[S-1][F-1]=-1

outfile.write(str(dist[S-1][F-1]))
infile.close()
outfile.close()