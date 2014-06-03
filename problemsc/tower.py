__author__ = 'Антон Брагин'

def get_component(people, languages):
    #Creating hybrid bipartite graph
    graph = []
    for language in languages:
        graph.append([50 + x for x in language])
    graph += people
    visited = [0] * len(graph)
    dfs(graph, visited, 50)
    #Account for visited people nodes only
    return sum(visited[50:])

def dfs(graph, visited, node):
    visited[node] = 1
    for next in graph[node]:
        if not visited[next]:
            dfs(graph, visited, next)

if __name__ == '__main__':
    with open('tower.in') as f:
        n = int(f.readline())
        language_knowledge = []
        for line in f:
            language_knowledge.append([int(x) for x in line.split()])
    people = []
    languages = [[] for _ in range(50)]
    #Create bipartite graph of peoples and languages
    for man, lk in enumerate(language_knowledge):
        man_languages = []
        #Create people->language and language->people mapping
        for i in range(1, len(lk)):
            man_languages.append(lk[i] - 1)
            languages[lk[i] - 1].append(man)
        people.append(man_languages)
    people_acknowledged = get_component(people, languages)
    with open('tower.out', 'w') as f:
        f.write(str(people_acknowledged))
