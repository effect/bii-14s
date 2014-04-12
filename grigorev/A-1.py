#!/usr/bin/python
from __future__ import division
import sys
from collections import deque

def graphFromData(inputData):
	graph = lambda: None
	graph.body = {}
	[graph.V, graph.E] = [int(x) for x in inputData[0].split()]
	for edgeDescription in inputData[1:]:
		[start, end] = [int(x) for x in edgeDescription.split()]
		graph.body[start] = graph.body.get(start, []) + [end  ]
		graph.body[end  ] = graph.body.get(end,   []) + [start]
	for vertex in range(1, graph.V + 1):
		if vertex not in graph.body:
			graph.body[vertex] = []
	return graph

def depthFirstSearch(graph):
	# vertex: componentToWhichItBelongs
	components = {}
	# assume 0 components initially
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
	sys.stdin  = open("components.in",  "r")
	sys.stdout = open("components.out", "w")
	graph      = graphFromData(sys.stdin.readlines())
	components = depthFirstSearch(graph)
	# number of components
	print(max(components.values()))
	# what vertex belongs where
	print(" ".join([str(x) for x in components.values()]))

main()
