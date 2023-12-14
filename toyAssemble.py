import sys
from collections import deque
sys.stdin = open('stdin', 'r')

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = {i : [] for i in range(n+1)}

costs = [0]*(n+1)
indegree = [0]*(n+1)

for _ in range(m):
    x, y, k = map(int, sys.stdin.readline().split())
    graph[x].append((y, k))
    indegree[y] +=1

base_parts = []

for i in range(1, len(graph)):
    if not graph[i]:
        base_parts.append(i)

def topology_sort(graph, indegree):
    queue = deque()
    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            queue.append(i)
            costs[i] = 1

    while queue:
        now_part = queue.popleft()

        for next_part, next_cost in graph[now_part]:
            
            indegree[next_part] -= 1
            costs[next_part] += next_cost*costs[now_part]
            
            if indegree[next_part] == 0:
                queue.append(next_part)

topology_sort(graph, indegree)

for i in base_parts:
    print(i, costs[i])