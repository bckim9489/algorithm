import sys
from collections import deque
sys.stdin = open('stdin', 'r')

n = int(sys.stdin.readline())
graph = []
visited = [[False]*n for _ in range(n)]
cost = [[float("inf")]*n for _ in range(n)]

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

for _ in range(n):
    row = list(map(int, sys.stdin.readline().strip()))
    graph.append(list(map(lambda x: (x-1)*-1, row)))

def zero_one_bfs(start:tuple):
    queue = deque()
    queue.append(start)
    cost[0][0] = 0

    while queue:
        now_cost, now_y, now_x = queue.popleft()
        if now_y == n-1 and now_x == n-1:
            print(now_cost)
            break

        for i in range(4):
            nx, ny = now_x+dx[i], now_y+dy[i]

            if 0 <= nx < n and 0 <= ny < n :
                if now_cost + graph[nx][ny] < cost[nx][ny]:
                    cost[nx][ny] = now_cost + graph[nx][ny]

                    if graph[nx][ny] == 0:
                        queue.appendleft((now_cost + graph[nx][ny], ny, nx))
                        continue

                    if graph[nx][ny] == 1:
                        queue.append((now_cost + graph[nx][ny], ny, nx))
                        continue   
    return
zero_one_bfs((0, 0, 0))
