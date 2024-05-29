import sys
from collections import deque

n, m, v =  map(int, sys.stdin.readline().split())

graph = [[0]*(n) for _ in range(n+1)]

visited_dfs = [False]*n
visited_bfs = [False]*n

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

def dfs(arr, i, visited):
    stack = [i]

    while stack:
        node = stack.pop()

        if not visited[node]:
            visited[node] = True
            print((node+1), end=" ")
            for j in range(len(arr[node])-1, -1, -1):
                if arr[node][j] != 0 and not visited[j]:
                    stack.append(j)

def bfs(arr, i, visited):
    queue = deque()
    queue.append(i)

    while queue:
        node = queue.popleft()

        if not visited[node]:
            visited[node] = True
            print((node+1), end=" ")
            for j in range(len(arr[node])):
                if arr[node][j] != 0 and not visited[j]:
                    queue.append(j)

dfs(graph, v-1, visited_dfs)
print("")
bfs(graph, v-1, visited_bfs)