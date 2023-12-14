import sys
from collections import deque

INF = 1000001
n, m, k, x = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u - 1].append(v - 1)

costs = [INF] * n
answer = []

def bfs(graph, start):
    queue = deque()
    queue.append(start)
    costs[start] = 0

    while queue:
        now = queue.popleft()
            
        for next_city in graph[now]:
            if costs[next_city] == INF:
                queue.append(next_city)
                costs[next_city] = costs[now] + 1

bfs(graph, x - 1)

for i in range(n):
    if costs[i] == k:
        answer.append(i)

if not answer:
    print(-1)
else:
    for i in answer:
        print(i + 1)