
import sys
import threading
 
def main():
 
   # read number of vertices
   f = open('pathbge1.in')
   v, e = (int(i) for i in f.readline().strip().split())
 
 
   #adjacency list
   adjacency_list=[[] for i in range(v)]
   for edge in f:
       x, y = ((int(i) - 1) for i in edge.strip().split())
       adjacency_list[x].append(y)
       adjacency_list[y].append(x)
 
   #bfs
   visited = [False] * v
   distance = [-1 for i in range(v)]
 
   def bfs(start, adjacency_list):
       queue = [start]
       visited[start] = True
       distance[start] = 0 # distance from start vertex to current one
       while len(queue) > 0:
            
           x = queue.pop(0)
 
           for i in adjacency_list[x]:
                   if visited[i] == False:
                       queue.append(i)
                       visited[i] = True
                       if distance[i] == -1:
                          distance[i] = distance[x] + 1
       return distance
 
   #write to file
 
   ans = open('pathbge1.out', 'w')
   for w in bfs(0, adjacency_list):
        ans.write(str(int(w)) + ' ')
   ans.close()
 
 
threading.stack_size(2 ** 26) # 64 MB stack size
sys.setrecursionlimit(1000000000) # recursion depth
thread = threading.Thread(target=main)
thread.start()