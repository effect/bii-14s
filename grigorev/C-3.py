#!/usr/bin/python
from __future__ import division

def interpret(lines):
	people = {} # {person: [languages, they, speak]}
	languages = {} # {language: [people, who, speak, it]}
	for person, line in list(enumerate(lines))[1:]:
		people[person] = [
			int(x) for x in
			line.split()[1:]
		]
		for language in people[person]:
			languages[language] = languages.get(language, []) + [person] # append or create
	return people, languages

def trace(start, visited):
	visited[start] = True
	for language in people[start]:
		for neighbor in languages[language]:
			if not visited[neighbor]:
				trace(neighbor, visited)

with open("tower.in") as infile:
	people, languages = interpret(infile.readlines())

visited = {
	person: False
	for person in people.keys()
}

trace(
	start = 1,
	visited = visited
)

with open("tower.out", "w") as outfile:
	outfile.write(str(visited.values().count(True)))
