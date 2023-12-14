import sys
from collections import deque
sys.stdin =open('stdin', 'r')

n, m = map(int, sys.stdin.readline().split())
graph = []
result_graph = []

max_berg = 0
iceCnt = 0
for y in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    for x in range(len(row)):
        if row[x] != 0:
            iceCnt += 1
    graph.append(row)
    

dx, dy = [1,-1,0,0], [0,0,1,-1]

def bundaberg(start):
    queue = deque()
    queue.append(start)
    cnt = 0
    while queue:
        now_y, now_x = queue.popleft()
        if not visited[now_y][now_x]:
            visited[now_y][now_x] = True
            cnt += 1
            for i in range(4):
                nx, ny = now_x + dx[i], now_y + dy[i]

                if 0 <= nx < m and 0 <= ny < n:
                    if graph[ny][nx] > 0:
                        queue.append((ny, nx))
                    else:
                        after_graph[now_y][now_x] -= 1
            
    
    return cnt

ice_age = 0

while True:
    visited = [[False]*m for _ in range(n)]
    after_graph = [[0]*m for _ in range(n)]
    result_graph = [[0]*m for _ in range(n)]
    sum_data = 0
    start_finder = ()
    for i in range(1, n):
        if sum(graph[i]) > 0:
            for j in range(1, m):
                if graph[i][j] != 0:
                    start_finder = (i, j)
                    break
        if start_finder:
            break

    cnt = bundaberg(start_finder)

    if iceCnt != cnt:
        print(ice_age)
        break

    ice_age += 1

    for i in range(n):
        for j in range(m):
            result_graph[i][j] = graph[i][j] + after_graph[i][j]
            if result_graph[i][j] < 0:
                result_graph[i][j] = 0
            if result_graph[i][j] == 0 and graph[i][j] != 0:
                iceCnt -= 1

        sum_data += sum(result_graph[i])

    if sum_data == 0:
        print(0)
        break

    graph = result_graph