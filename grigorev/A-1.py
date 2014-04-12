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


""" Perform a depth-first search on a graph.                                 """
""" Return "components" (a dictionary of following structure):               """
"""        key = vertex                                                      """
"""        value = number of component to which it belongs                   """
def depthFirstSearch(graph):
	components = {}
	currentComponent = 0
	# NB! vertices start from 1 and go up to V inclusive
	for vertex in range(1, graph.V + 1):
		# if we haven't yet visited this vertex
		if vertex not in components:
			# it's a new component
			currentComponent += 1
			components[vertex] = currentComponent
			# put it into the queue, as Fedor taught
			queue = deque([vertex])
			# queue up its immediate neighbors
			while len(queue) > 0:
				for neighbor in graph.body[queue[0]]:
					# if we haven't yet visited the neighbor
					if neighbor not in components:
						# it's connected, so it's the same component
						components[neighbor] = currentComponent
						queue.append(neighbor)
				queue.popleft()
	return components


def main():
	# using sys.std* handles for ease of local debugging
	sys.stdin  = open("components.in",  "r")
	sys.stdout = open("components.out", "w")
	graph      = adjacencyListFromData(sys.stdin.readlines())
	components = depthFirstSearch(graph)
	# number of components
	print(max(components.values()))
	# what vertex belongs where
	print(" ".join([str(x) for x in components.values()]))

main()
