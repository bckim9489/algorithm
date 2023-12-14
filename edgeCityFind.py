import sys
from collections import deque
sys.stdin = open('stdin', 'r')

INF = 1000001
n, m, k, x = map(int, sys.stdin.readline().split())

graph = [[0]*n for _ in range(n)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u-1][v-1] = 1

costs = [INF]*n
answer = []
def bfs(graph, start):
    queue = deque()
    queue.append(start)
    costs[start] = 0

    while queue:
        now = queue.popleft()
            
        for i in range(len(graph[now])):
            if graph[now][i] != 0:
                queue.append(i)
                if costs[i] > graph[now][i]+costs[now]:
                    costs[i] = graph[now][i]+costs[now]        
        
    return

bfs(graph, x-1)

for i in range(len(costs)):
    if costs[i]==k:
        answer.append(i)

if len(answer) == 0:
    print(-1)
else :
    for i in answer:
        print(i+1)

    