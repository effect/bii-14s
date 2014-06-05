
import sys
import threading
 
 
 
def main():
 
    # read number of vertices
    f = open('components.in')
    first_string = f.readline().strip().split(' ')
    n = int(first_string[0])
 
    #read edges list
    next_string = ' '
    edges_list = []
    inner_list = []
    while next_string != ['']:
        next_string = f.readline().strip().split(' ')
        if next_string != ['']:
            inner_list.append(int(next_string[0])-1)
            inner_list.append(int(next_string[1])-1)
            edges_list.append(inner_list)
        inner_list = []
    f.close()
 
    # make full edges list with reverse edges
    rev_edges_list = []
    for i in edges_list:
        a = i[::-1]
        rev_edges_list.append(a)
    full_edges_list = edges_list + rev_edges_list
 
    #convert edges list to adjacency list
    adjacency_list = []
 
    for i in range(n):
        adjacency_list.append([])
 
    for i in full_edges_list:
        a = (i[0])
        adjacency_list[a].append(i[1])
 
    #dfs
    visited = [False] * n
    comp_number = 0
    components_list = [-1] * n
 
    def dfs(v):
        components_list[v] = comp_number
        visited[v] = True
        for w in adjacency_list[v]:
            if not visited[w]:
                dfs(w)
 
    #counting components
    for v in range(n):
        if not visited[v]:
            dfs(v)
            comp_number += 1
 
 
    #write to file
     
    ans = open('components.out', 'w')
    ans.write(str(comp_number) + '\n')
    for w in components_list:
        ans.write(str(int(w) + 1) + ' ')
    ans.close()
 
 
threading.stack_size(2 ** 26) # 64 MB stack size
sys.setrecursionlimit(1000000000) # recursion depth
thread = threading.Thread(target=main)
thread.start()