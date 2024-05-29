import sys
sys.setrecursionlimit(10**9)

n, m = map(int, sys.stdin.readline().split())

graph = {i:[] for i in range(n+1)}
visited = [False]*(n+1)
result = []
route = []

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    if v in graph:
        graph[v].append(u)

def dfs(graph, start):
    
    if visited[start]:
        return 

    visited[start] = True
    route.append(start)

    for now in graph[start]:
        dfs(graph, now)
   
for i in range(1, n+1):
    route = []
    dfs(graph, i)
    if route:
        result.append(route)

print(len(result))