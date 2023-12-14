import sys
from collections import deque
sys.stdin = open('stdin', 'r')

n, m = map(int, sys.stdin.readline().split())
visited = [[False]*m for _ in range(n)]
graph = []
'''
offset
'''
dx, dy = [1,-1,0,0], [0,0,1,-1]

for _ in range(n):
    row = list(map(str, sys.stdin.readline().strip()))
    graph.append(row)


def bfs():
    queue = deque()
    queue.append((0,0))
    
    cnt = 1

    while queue:
        now_y, now_x = queue.popleft()
        if not visited[now_y][now_x]:
            visited[now_y][now_x] = True
            for i in range(4):
                nx, ny = now_x + dx[i], now_y + dy[i]
                if 0<= nx < m and 0<= ny < n:
                    if graph[now_y][now_x] == graph[ny][nx]:
                        if graph[now_y][now_x] == '-':
                            if i == 0:
                                queue.append((ny, nx))
                                continue
                            if i == 2:
                                cnt+=1
                                queue.append((ny, nx))
                                continue
                        if graph[now_y][now_x] == '|':
                            if i == 2:
                                queue.append((ny, nx))
                                continue
                            if i == 0:
                                cnt+=1
                                queue.append((ny, nx))
                                continue

                    if graph[now_y][now_x] != graph[ny][nx]:
                        if graph[now_y][now_x] == '-':
                            if i == 0:
                                cnt+=1
                                queue.append((ny, nx))
                                continue
                            if i == 2:
                                queue.append((ny, nx))
                                continue
                        if graph[now_y][now_x] == '|':
                            if i == 2:
                                cnt+=1
                                queue.append((ny, nx))
                                continue
                            if i == 0:
                                cnt+=1
                                queue.append((ny, nx))
                                continue

    return cnt

print(bfs())
            
                