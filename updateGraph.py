import sys
sys.stdin = open('stdin', 'r')
from collections import deque

n = int(sys.stdin.readline())
indegree = [0]*(n+1)

graph = {i : [] for i in range(n+1)}
update_dict = {i : i for i in range(n+1)}
for j in range(1, n+1):
    row = list(map(int, sys.stdin.readline().strip()))
    for i in range(n):
        if row[i] != 0:
            graph[i+1].append(j)
            indegree[j] +=1

print(graph)
print(indegree)
def topology_sort():
    queue = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)
    
    if not queue:
        return -1

    while queue:
        now = queue.popleft()

        for next_node in graph[now]:
            if update_dict[now] < update_dict[next_node]:
                update_dict[now], update_dict[next_node] = update_dict[next_node], update_dict[now]
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    queue.append(next_node)
    return 1
result = topology_sort()
if result == 1:
    for i in range(1, n+1):
        print(update_dict[i], end=' ')
else : print(-1)
'''
'''
                
            


