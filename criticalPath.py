import sys
from collections import deque
sys.stdin = open('stdin', 'r')

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = {i : [] for i in range(n+1)}
graph_usd = {i : [] for i in range(n+1)}
indegree = [0]*(n+1)
costs = [0]*(n+1)
visited_usd = [False]*(n+1)
for _ in range(m):
    u, v, cost = map(int, sys.stdin.readline().split())
    graph[u].append((v, cost))
    graph_usd[v].append((u, cost))
    indegree[v] += 1

start, end = map(int, sys.stdin.readline().split())

def topology_sort():
    queue = deque()
    queue.append((start, 0))

    while queue:
        now_city, now_cost = queue.popleft()

        for next_city, next_cost in graph[now_city]:
            indegree[next_city] -= 1
            if costs[next_city] < now_cost+next_cost:
                costs[next_city] = now_cost+next_cost

            if indegree[next_city] == 0:                
                queue.append((next_city, costs[next_city]))
    
    queue.append((end, 0))
    cnt = 0
    while queue:
        now_city, now_cost = queue.popleft()
        for past_city, past_cost in graph_usd[now_city]:
            if costs[now_city] == costs[past_city] + past_cost:
                cnt +=1
                if not visited_usd[past_city]:
                    visited_usd[past_city] =True
                    queue.append((past_city, past_cost))
    
    return cnt
            
result_cnt = topology_sort()
print(costs[end])
print(result_cnt)