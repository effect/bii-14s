__author__ = 'Антон Брагин'

import sys
from collections import deque

#Set it if you are planning to use DFS
sys.setrecursionlimit(200000)

#This is C-style graph representation that is extremely unnatural for Python
#But I wasn't able to found object-based solution that could pass time tests
class Graph:

    def __init__(self, vertices, edges):
        """
        Initialize graph object

        :param vertices: number of vertices in the graph (nonzero by definition)
        :param edges: number of edges in the graph
        """
        self.vertices = vertices
        self.head = [-1 for i in range(vertices)]
        self.component = [-1 for i in range(vertices)]
        self.next = [-1 for i in range(2 * edges)]
        self.edge = [-1 for i in range(2 * edges)]

        self.edge_counter = 0

    def addEdge(self, v, w):
        """
        Add edge to graph

        :param v: edge source
        :param w: edge sink
        :return: void
        """
        #Skip self-edges
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
        """
        Run DFS from the vertex specified and mark components

        :param v: vertex to start from
        :param component: current component
        """
        self.component[v] = component

        e = self.head[v]
        while e >= 0:
            w = self.edge[e]

            if self.component[w] == -1:
                self.dfs(w, component)

            e = self.next[e]

    def bfs(self, v, component):
        """
        Run BFS from the vertex specified and mark components

        :param v: vertex to start from
        :param component: current component
        """
        vertices_deque = deque()
        vertices_deque.append(v)

        while len(vertices_deque) > 0:
            current = vertices_deque.popleft()
            self.component[current] = component

            e = self.head[current]
            while e >= 0:
                w = self.edge[e]

                if self.component[w] == -1:
                    vertices_deque.append(w)

                e = self.next[e]

def create_graph(file_in):
    """
    Create grapth from the file provided

    :param file_in: file to read graph from
    :return: Graph object
    """
    with open(file_in) as f:
        nm = [int(x) for x in f.readline().split()]

        graph = Graph(nm[0], nm[1])
        for line in f:
            if len(line.strip()) > 0:
                vx = [int(x) for x in line.split()]
                graph.addEdge(vx[0], vx[1])

    return graph

def get_components(graph):
    """
    Mark graph vertices by components they belong to

    :param graph: Graph object to analyze
    :return: number of graph components
    """
    comp = 0
    for i in range(graph.vertices):
        if graph.component[i] == -1:
            comp += 1
            graph.bfs(i, comp)

    return comp

def print_components(file_out, graph, ncomp):
    """
    Print output to the file specified

    :param file_out: path to the output file
    :param graph: Graph object to print
    :param ncomp: numer of graph components
    """
    with open(file_out, 'w') as f:
        f.write(str(ncomp))
        f.write('\n')
        for vc in graph.component:
            f.write(str(vc))
            f.write(' ')

#Execute
graph = create_graph('components.in')
ncomp = get_components(graph)
print_components('components.out', graph, ncomp)