import sys
from collections import deque
sys.stdin = open('stdin', 'r')

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)] #1번 부터

indegree = [0]*(n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort(graph, indegree):
    queue = deque()
    result = []
    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        for next_child in graph[now]:
            indegree[next_child] -= 1
            if indegree[next_child] == 0:
                queue.append(next_child)

        result.append(now)

    return result
        
print(*topology_sort(graph, indegree))


    


