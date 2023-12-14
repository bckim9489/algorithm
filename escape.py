import sys
from collections import deque
sys.stdin = open('stdin', 'r')

graph = []
r, c = map(int, sys.stdin.readline().split())
dx, dy = [1,-1, 0, 0],[0, 0, 1,-1]
start = []
water_start = []


for i in range(r):
    row = list(map(str, sys.stdin.readline().strip()))
    if 'S' in row:
        start.append((0, i, row.index('S')))
    if '*' in row:
        water_start.append((i, row.index('*')))

    graph.append(row)


def bfs(water_start, dochi_start):
    dochi_queue = deque(dochi_start) #도치형님
    watar_queue = deque(water_start) #물선생님

    while dochi_queue:
        #물선생님 무빙
        for _ in range(len(watar_queue)):
            now_watar_y, now_watar_x = watar_queue.popleft()

            for i in range(4):
                nx, ny = now_watar_x + dx[i], now_watar_y + dy[i]
                if 0<= nx < c and 0<= ny < r:
                    if graph[ny][nx] == '.':
                        graph[ny][nx] = '*'
                        watar_queue.append((ny, nx))
        
        for _ in range(len(dochi_queue)):
            #도치형님 무빙
            now_cost, now_dochi_y, now_dochi_x = dochi_queue.popleft()

            for i in range(4):
                ny, nx = now_dochi_y + dy[i], now_dochi_x + dx[i]
                if 0<= nx < c and 0<= ny < r :
                    if graph[ny][nx] == 'D':
                        return print(now_cost+1)
                    
                    if graph[ny][nx] == '.':
                        dochi_queue.append((now_cost+1, ny, nx))
                        graph[ny][nx] = 'X'
    return print('KAKTUS')
    
bfs(water_start, start)

