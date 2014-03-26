__author__ = 'Антон Брагин'

import sys

sys.setrecursionlimit(200000)

class Graph:

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.head = [-1 for i in range(vertices)]
        self.component = [-1 for i in range(vertices)]
        self.next = [-1 for i in range(2 * edges)]
        self.edge = [-1 for i in range(2 * edges)]

        self.edge_counter = 0

    def addEdge(self, v, w):
        if (v == w):
            return
        #Convert to zero based
        v -= 1
        w -= 1

        self.edge[self.edge_counter] = w
        self.next[self.edge_counter] = self.head[v]
        self.head[v] = self.edge_counter
        self.edge_counter += 1

        self.edge[self.edge_counter] = v
        self.next[self.edge_counter] = self.head[w]
        self.head[w] = self.edge_counter
        self.edge_counter += 1

    def dfs(self, v, component):
        #print('dfs from {}'.format(v))
        self.component[v] = component

        e = self.head[v]
        while e >= 0:
            w = self.edge[e]

            if self.component[w] == -1:
                self.dfs(w, component)

            e = self.next[e]

def create_graph(file_in):
    with open(file_in) as f:
        nm = [int(x) for x in f.readline().split()]

        graph = Graph(nm[0], nm[1])
        for line in f:
            if len(line.strip()) > 0:
                vx = [int(x) for x in line.split()]
                #Self connections does not affects components
                graph.addEdge(vx[0], vx[1])
    #print(graph.head, graph.edge, graph.next)

    return graph

def get_components_dfs(graph):
    comp = 0
    for i in range(graph.vertices):
        #print(graph.component)
        if graph.component[i] == -1:
            comp += 1
            graph.dfs(i, comp)

    return comp

def print_components(file_out, graph, ncomp):
    with open(file_out, 'w') as f:
        f.write(str(ncomp))
        f.write('\n')
        for vc in graph.component:
            f.write(str(vc))
            f.write(' ')

#Execute
#graph = create_graph('components.in')
#ncomp = get_components_dfs(graph)
#print_components('components.out', graph, ncomp)