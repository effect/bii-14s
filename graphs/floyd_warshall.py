__author__ = 'Антон Брагин'

def parse_input(file):
    with open(file) as f:
        n, m = [int(x) for x in f.readline().split()]

        #Create distances matrix. None is placeholder that will be replaces with +Inf
        d = [[None for j in range(n)] for i in range(n)]

        #Vertex always connected to itself with zero distance
        for i in range(n):
            d[i][i] = 0

        total_weight = 0
        #Read edges data
        for i in range(m):
            u, v, w = [int(x) for x in f.readline().split()]
            d[u - 1][v - 1] = w
            total_weight += w

        #Replace None with the value that is greater then any path in graph without negative edges
        for i in range(n):
            for j in range(n):
                if d[i][j] is None:
                    d[i][j] = total_weight + 1

        return n, d

def floyd_warshall(n, d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]

    return d

#Execute
n, d = parse_input('pathsg.in')
d = floyd_warshall(n, d)

#Write output
with open('pathsg.out', 'w') as fout:
    for row in d:
        fout.write(' '.join(str(x) for x in row))
        fout.write('\n')