import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('stdin', 'r')

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = {}
visited = [False]*(n+1)

def dfs(graph, start):
    if visited[start] or not graph:
        return
    
    visited[start] = True
    for now in graph[start]:
        dfs(graph, now)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())

    if u in graph:
        graph[u].append(v)
    else : 
        graph[u] = [v]

    if v in graph:
        graph[v].append(u)
    else : 
        graph[v] = [u]

dfs(graph, 1)
cnt = 0
visited[1] = False
for j in visited:
    if j:
        cnt +=1
        
print(cnt)