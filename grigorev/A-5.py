#!/usr/bin/python
from __future__ import division
import sys
from collections import deque

""" Reads input line per line. Expects first line to contain the number of   """
""" vertices and edges, all following lines are edges in format (u, v, w).   """
""" Returns an adjacency list (actually a dictionary) of structure:          """
"""         key = vertex                                                     """
"""         value = dict(neighbor, weight(vertex, neighbor))                 """
def adjacencyListFromData(inputData):
	# catch-all record
	graph = lambda: None
	# (V)ertices, (E)dges
	[graph.V, graph.E] = [int(x) for x in inputData[0].split()]
	# preinitialize adjacency list
	graph.body = {
		vertex: {}
		for vertex in range(graph.V)
	}
	# parse input
	for edgeDescription in inputData[1:]:
		# NB! convert vertex numbers to 0 through V-1
		[start, end, weight] = [int(x) for x in edgeDescription.split()]
		graph.body[start-1][end-1] = weight
	return graph


""" Returns initial approximation of distances.                              """
def initializeDistanceMatrix(graph):
	# arbitrary infinity == 1e1000
	distances = [[1e1000] * graph.V for _ in range(graph.V)]
	# self-loops of zero length
	for vertex in range(graph.V):
		distances[vertex][vertex] = 0
	# first approximation of distances between immediate neighbors
	for start in range(graph.V):
		for finish, weight in graph.body[start].iteritems():
			distances[start][finish] = weight
	return distances


""" Relax edges while possible, return resulting distance list.              """
def floydWarshall(distances, graph):
	for through in range(graph.V):
		for start in range(graph.V):
			for finish in range(graph.V):
				if distances[start][finish]:
					distances[start][finish] = min(
						distances[start][finish],
						distances[start][through] + distances[through][finish]
					)
	return distances


def main():
	# using sys.std* handles for ease of local debugging
	sys.stdin  = open("pathsg.in",  "r")
	sys.stdout = open("pathsg.out", "w")
	graph      = adjacencyListFromData(sys.stdin.readlines())
	distances  = initializeDistanceMatrix(graph)
	distances  = floydWarshall(distances, graph)
	for line in distances:
		print(" ".join(
			str(x)
			for x in line
		))

main()
