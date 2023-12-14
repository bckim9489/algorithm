import sys
from collections import deque
sys.stdin = open('stdin', 'r')

m, n, h = map(int, sys.stdin.readline().split())

graph = []
good_tomato = []
for p in range(h):
    panel = []
    
    for q in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        panel.append(row)
        for i in range(m):
            if row[i] == 1:
                tmp_d_h_n_m = (0, p, q, i)
                good_tomato.append(tmp_d_h_n_m)
    graph.append(panel)

visited = [[[False]*m for _ in range(n)] for __ in range(h)]

dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]

def bfs(start_list):
    queue = deque(start_list)
    result_day = 0
    while queue:
        now_day, now_z, now_y, now_x = queue.popleft()
        if not visited[now_z][now_y][now_x]:
            visited[now_z][now_y][now_x] = True
            graph[now_z][now_y][now_x] = 1
            result_day = now_day
            for j in range(6):
                nz, ny, nx = dz[j]+now_z, dy[j]+now_y, dx[j]+now_x
                if 0 <= nz < h and 0<= ny < n and 0<= nx < m and graph[nz][ny][nx] == 0:
                    queue.append((now_day+1, nz, ny, nx))

    return result_day

day = bfs(good_tomato)
flag = True

for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                flag = False
                break
if flag: 
    print(day) 
else : 
    print(-1)


        