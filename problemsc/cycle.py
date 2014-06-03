__author__ = 'Антон Брагин'

import sys
import threading

sys.setrecursionlimit(1000000)

def find_cycle(graph):
    #State codes: 0 - non-visited, 1 - visiting, 2 - closed
    state = [0] * len(graph)
    parent = [None] * len(graph)
    for i in range(len(graph)):
        if state[i] == 0:
            cycle = dfs(graph, state, parent, i)
            if cycle:
                return cycle
    return None

def dfs(graph, state, parent, index):
    state[index] = 1
    for child in graph[index]:
        parent[child] = index
        if state[child] == 0:
            cycle = dfs(graph, state, parent, child)
            if cycle is not None:
                return cycle
        if state[child] == 1:
            #Cycle found
            return get_cycle(parent, child, child)
    state[index] = 2
    return None

def get_cycle(parent, start, end):
    cycle = [end]
    while parent[end] != start:
        previous = parent[end]
        cycle.append(previous)
        end = previous
    return cycle

def main():
    with open('cycle.in') as f:
        n, m = [int(x) for x in f.readline().split()]
        graph = [[] for _ in range(n)]
        for _ in range(m):
            fr, to = [int(x) for x in f.readline().split()]
            graph[fr - 1].append(to - 1)
    cycle = find_cycle(graph)
    with open('cycle.out', 'w') as f:
        if cycle:
            cycle.reverse()
            cycle = ' '.join([str(x + 1) for x in cycle])
            f.write('YES\n')
            f.write(cycle)
        else:
            f.write('NO\n')

if __name__ == '__main__':
    threading.stack_size(2 ** 26) #64 MB stack size
    sys.setrecursionlimit(2 ** 20) #recursion depth
    thread = threading.Thread(target=main)
    thread.start()
