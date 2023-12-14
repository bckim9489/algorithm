import sys
import heapq

n = int(sys.stdin.readline()) #vertax
m = int(sys.stdin.readline()) #arc
graph = {i:[] for i in range(n+1)}

MAX = sys.maxsize
costs = {i: MAX for i in range(n + 1)}

for _ in range(m):
    u, v, cost = map(int, sys.stdin.readline().split())
    graph[u].append((v, cost))

start, end = map(int, sys.stdin.readline().split())


def dijkstra(start_node):
    queue = []
    heapq.heappush(queue, (0, start_node))
    costs[start_node] = 0
    while queue:
        now_cost, now_node = heapq.heappop(queue)
        if now_cost > costs[now_node]:
            continue
        if now_node == end:
            print(now_cost)
            exit()
        for next_node, next_cost in graph[now_node]:
            if costs[next_node] > (next_cost+now_cost):
                costs[next_node] = (next_cost+now_cost)
                heapq.heappush(queue, (now_cost+next_cost, next_node))
                
    return

dijkstra(start)