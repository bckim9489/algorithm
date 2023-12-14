import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('stdin', 'r')

n, m = map(int, sys.stdin.readline().split())
min_graph = {i :[] for i in range(n+1)}
max_graph = {i :[] for i in range(n+1)}

max_costs = [0]*(n+1)
min_costs = [0]*(n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    min_graph[a].append(b)
    max_graph[b].append(a)

def dfs(graph, start, costs, visited):
    if not visited[start]:
        costs[start] += 1  
        visited[start] = True
        for next_node in graph[start]:
            dfs(graph, next_node, costs, visited)  

for i in range(1, n+1):
    max_visited = [False]*(n+1)
    min_visited = [False]*(n+1)
    dfs(max_graph, i, max_costs, max_visited)
    dfs(min_graph, i, min_costs, min_visited)

cnt = 0

for i in range(1, n+1):
    if max_costs[i] > ((n+1)/2):
        cnt+=1
    if min_costs[i] > ((n+1)/2):
        cnt+=1
print(cnt)
