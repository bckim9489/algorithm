import sys
sys.stdin = open('stdin', 'r')
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
in_and_out = [0]+list(map(int, sys.stdin.readline().strip()))
cnt = 0

visited = [False]*(n+1)

for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    if in_and_out[u] ==1 and in_and_out[v] ==1:
        cnt += 2
        
def dfs(start, nodeCnt):
    
    visited[start] = True

    for next_node in graph[start]:
        if in_and_out[next_node] == 1:
            nodeCnt += 1
        elif not visited[next_node] and in_and_out[next_node] == 0:
            nodeCnt = dfs(next_node, nodeCnt)
    return nodeCnt


for i in range(1, n+1):
    if in_and_out[i] == 0 and not visited[i]:
        res = dfs(i, 0)
        cnt += res*(res-1)
    
print(cnt)