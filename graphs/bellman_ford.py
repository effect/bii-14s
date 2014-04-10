__author__ = 'Антон Брагин'

class Graph:

    def __init__(self, n, edges, total_weight):
        """
        Create graph representation suitable for Bellman-Ford traversal

        :param n: number of vertices
        :param edges: tuples of form (edge source, edge sink, edge weight)
        :param total_weight: total weight of edges in the graph (assuming they all are non negative)
        """
        self.n = n
        self.edges = edges
        #In graph with positive edge weights path longer then total_weight + 1 can't exist
        self.distances = [total_weight + 1 for i in range(n)]

    def find_distance(self, start, finish):
        self.distances[start - 1] = 0

        for i in range(1, self.n):
            for u, v, w in self.edges:
                if self.distances[v] > self.distances[u] + w:
                    self.distances[v] = self.distances[u] + w

        return self.distances[finish - 1]

def parse_input(file):
    with open(file) as fin:
        n, s, f = [int(x) for x in fin.readline().split()]
        total_weight = 0

        edges = []

        for u in range(n):
            adjacent = [int(x) for x in fin.readline().split()]
            for v, w in enumerate(adjacent):
                if w != -1 and u != v:
                    edges.append((u, v, w))
                    total_weight += w

        return n, edges, s, f, total_weight

#Execution
n, edges, s, f, total_weight = parse_input('pathmgep.in')
graph = Graph(n, edges, total_weight)
d = graph.find_distance(s, f)

with open('pathmgep.out', 'w') as fout:
    if d <= total_weight:
        fout.write(str(d))
    else:
        fout.write(str(-1))
