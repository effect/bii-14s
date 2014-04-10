__author__ = 'Антон Брагин'

import math
from operator import itemgetter

class DSU:
    '''
    Disjoint set union implementation with paths compression and ranks heuristics implemented
    '''

    def __init__(self, n):
        """
        Create set of size n where each element is the parent of itself.

        :param n: number of different elements/sets
        """
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find_set(self, v):
        """
        Find set to which element belongs.

        :param v: element to search
        :return: number of set
        """
        if v == self.parent[v]:
            return v
        else:
            self.parent[v] = self.find_set(self.parent[v])
            return self.parent[v]

    def union_sets(self, u, v):
        """
        Unite the sets provided.

        :param u: first set to unite
        :param v: second set to unite
        """
        uset = self.find_set(u)
        vset = self.find_set(v)

        if uset != vset:
            if self.size[uset] < self.size[vset]:
                self.parent[uset] = vset
                self.size[vset] += self.size[uset]
            else:
                self.parent[vset] = uset
                self.size[uset] += self.size[vset]

def parse_input(file):
    """
    Read input from the file provided and return graph.

    :param file: file to read data from
    :return: tuple with number of graph vertices and list of tuples containing source vertex, sink vertex, edge weight
    """
    with open(file) as fin:
        n = int(fin.readline().strip())
        coordinates = []
        for e in range(n):
            x, y = [float(x) for x in fin.readline().split()]
            #Append coordinate pair
            coordinates.append((x, y))

        #Generate all possible edges of complete graph and distances between them
        edges = []
        #Calculate distances between vertices
        for u in range(len(coordinates)):
            for v in range(u, len(coordinates)):
                if u != v:
                    p1 = coordinates[u]
                    p2 = coordinates[v]
                    edges.append((u, v, math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2))))

        return n, edges

def kruskal(n, edges):
    """
    Runs Kruskal algorithm and return minimum spanning tree size.

    :param n: number of vertices in the graph
    :param edges: graph edges
    :return: size of minimum spanning tree
    """
    edges = sorted(edges, key=itemgetter(2))
    dsu = DSU(n)

    tree_size = 0

    for edge in edges:
        u, v, d = edge
        if dsu.find_set(u) != dsu.find_set(v):
            dsu.union_sets(u, v)
            tree_size += d


    return tree_size

#Execute
n, edges = parse_input('spantree.in')
tree_size = kruskal(n, edges)

#Write output
with open('spantree.out', 'w') as fout:
    fout.write(str(tree_size))
