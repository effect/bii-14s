#!/usr/bin/python
from __future__ import division
import sys
from collections import deque

""" Reads input line per line. Expects first line to contain the number of   """
""" vertices and edges, all following lines are edges in format (u, v).      """
""" Returns an adjacency list (actually a dictionary).                       """
def adjacencyListFromData(inputData):
	# catch-all record
	graph = lambda: None
	# (V)ertices, (E)dges
	[graph.V, graph.E] = [int(x) for x in inputData[0].split()]
	# preload adjacency list
	graph.body = {
		vertex: []
		for vertex in xrange(1, graph.V + 1)
	}
	# parse input
	for edgeDescription in inputData[1:]:
		# undirected graph, draw edges both ways
		[start, end] = [int(x) for x in edgeDescription.split()]
		graph.body[start].append(end  )
		graph.body[end  ].append(start)
	return graph


""" Perform a breadth-first search on a graph.                               """
""" Return "distances" (a dictionary of following structure):                """
"""        key = vertex                                                      """
"""        value = distance from startVertex                                 """
def breadthFirstSearch(graph, startVertex):
	# start lookup from the initial vertex
	queue = deque([startVertex])
	distances = {startVertex: 0}
	# all edges are explicitly the same length (BFS won't work otherwise)
	edgeLength = 1
	# while there's still vertices to process
	while len(queue):
		# look up neighbors of current vertex
		for neighbor in graph.body[queue[0]]:
			# if we haven't visited the neighbor yet
			if neighbor not in distances:
				distances[neighbor] = distances[queue[0]] + edgeLength
				queue.append(neighbor)
		queue.popleft()
	return distances


def main():
	# using sys.std* handles for ease of local debugging
	sys.stdin  = open("pathbge1.in",  "r")
	sys.stdout = open("pathbge1.out", "w")
	graph      = adjacencyListFromData(sys.stdin.readlines())
	distances  = breadthFirstSearch(graph, 1)
	print(" ".join([str(x) for x in distances.values()]))

main()
