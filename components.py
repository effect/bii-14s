__author__ = 'abragin'

import logging
import sys

sys.setrecursionlimit(200000)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))

class Graph:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.vertices = [[] for i in range(n)]
        self.component = [None for i in range(n)]

    def __str__(self):
        str_repr = 'Vertices: ' + str(self.n) + ' Edges: ' + str(self.m) + '\n'
        for i, v in enumerate(self.vertices):
            str_repr = str_repr + '{} (comp {}) is connected to: {}'.format(str(i), self.component[i], str(v)) + '\n'
        return str_repr

def create_graph(file_in):
    with open(file_in) as f:
        nm = [int(x) for x in f.readline().split()]

        graph = Graph(nm[0], nm[1])
        for line in f:
            if len(line.strip()) > 0:
                vx = [int(x) for x in line.split()]
                #Self connections does not affects components
                if vx[0] != vx[1]:
                    graph.vertices[vx[0] - 1].append(vx[1] - 1)
                    graph.vertices[vx[1] - 1].append(vx[0] - 1)

    return graph

def get_components(graph):
    component = 0
    for i in range(graph.n):
        if graph.component[i] is None:
            component = component + 1
            dfs(graph, i, component)

    return component

def dfs(graph, i, component):
    logger.debug('Starting DFS from {}'.format(i))
    graph.component[i] = component
    for linked in graph.vertices[i]:
        if graph.component[linked] is None:
            dfs(graph, linked, component)

def print_components(file_out, graph, ncomp):
    with open(file_out, 'w') as f:
        f.write(str(ncomp))
        f.write('\n')
        for vc in graph.component:
            f.write(str(vc))
            f.write(' ')

#Execute script
#graph = create_graph('components.in')
#
#ncomp = get_components(graph)
#logger.debug('Graph analyzed: {}'.format(graph))
#
#print_components('components.out', graph, ncomp)