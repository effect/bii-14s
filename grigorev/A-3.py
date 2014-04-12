#!/usr/bin/python
from __future__ import division
import sys
from collections import deque

""" Expects input as space-separated incidence matrix. Converts str to int.  """
def incidenceMatrixFromData(inputData):
	graph = lambda: None
	graph.body = [
		[int(x) for x in line.split()]
		for line in inputData
	]
	graph.V = len(graph.body)
	graph.E = None
	return graph

""" Find weight of the shortest path from vertex "start" to vertex "finish"  """
""" using Dijkstra's algorightm.                                             """
""" Weights of paths are stored in the dictionary "distances" of structure:  """
"""         key = vertex                                                     """
"""         value = distance from "start"                                    """
""" Finishes as soon as distance is found for "finish". Returns one value.   """
""" If no path found (i.e. all cycles passed without returning a value),     """
""" returns -1.                                                              """
def dijkstra(graph, start, finish):
	# begin lookup from "start"
	distances = {
		vertex: None
		for vertex in xrange(graph.V)
	}
	distances[start] = 0
	# keep track of visited vertices
	visited = {
		vertex: False
		for vertex in xrange(graph.V)
	}
	# while there are unvisited vertices
	while visited.values().count(False):
		# find an unvisited vertex with a smallest tentative distance
		indices = [ # indices of unvisited vertices
			index
			for (index, value) in visited.iteritems()
			if not value
		]
		distancesToConsider = [ # distances of edges leading to these unvisited vertices
			distance
			for (index, distance) in distances.iteritems()
			if (index in indices)
		]
		# if there's no more distances to consider, we've hit a brick wall
		if distancesToConsider.count(None) == len(distancesToConsider):
			break
		# otherwise, find the next vertex to process
		vertex = indices[
			distancesToConsider.index(
				min([
					x for x in distancesToConsider
					if x != None
				])
			)
		]
		# to prevent looping onto itself, do this before proceedin
		visited[vertex] = True
		# relax all immediate edges leading to unvisited vertices
		for (neighbor, weight) in enumerate(graph.body[vertex]):
			if weight >= 0:
				if not visited[neighbor]:
					# if there's a value that's been assigned during a previous iteration
					if distances[neighbor]:
						distances[neighbor] = min(
							distances[vertex] + weight,
							distances[neighbor]
						)
					else:
						distances[neighbor] = (
							distances[vertex] + weight
						)
		# if finish vertex has been reached already
		if vertex == finish:
			return distances[finish]
	# if we haven't reached the finish vertex at all
	return -1


def main():
	# using sys.std* handles for ease of local debugging
	sys.stdin  = open("pathmgep.in",  "r")
	sys.stdout = open("pathmgep.out", "w")
	inputData  = sys.stdin.readlines()
	[_, S, F]  = [int(x)-1 for x in inputData[0].split()]
	graph      = incidenceMatrixFromData(inputData[1:])
	print(dijkstra(graph, S, F))

main()
