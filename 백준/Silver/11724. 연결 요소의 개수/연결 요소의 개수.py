import sys
sys.setrecursionlimit(10**9)
N, M = map(int, sys.stdin.readline().split())
g = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    g[u][v], g[v][u] = 1, 1

cnt = 0

def dfs(now, visited):
    if visited[now]:
        return 0

    visited[now] = 1
    for idx, value in enumerate(g[now]): 
        if value != 0 and visited[idx] == 0:
            dfs(idx, visited)
    return 1

for i in range(1, N+1):
    cnt += dfs(i, visited)

print(cnt)