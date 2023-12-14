import sys
sys.stdin = open('stdin', 'r')
from collections import deque

graph = []

n = int(sys.stdin.readline())
'''
offset
'''
dx, dy = [1,-1,0,0], [0,0,1,-1]

visited = [[False]*n for _ in range(n)]

for _ in range(n):
    row = list(map(int, sys.stdin.readline().strip()))
    graph.append(row)

danji = []
total_cnt = 0
def bfs(graph):
    queue = deque()
    queue.append((0,0))
    house_switch = False

    if graph[0][0] != 0:
        house_switch = True

    while queue:
        now_y, now_x = queue.popleft()
        if not visited[now_y][now_x]:
            visited[now_y][now_x] = True
            for i in range(4):
                nx, ny = now_x + dx[i], now_y+dy[i]
                if 0<= nx < n and 0<= ny < n:
                    if graph[ny][nx] == 0 and house_switch == False:
                        pass        
                    if graph[ny][nx] == 1 and house_switch == True:
                        cnt +=1

                    if graph[ny][nx] == 1 and house_switch == False:
                        house_switch == True
                        total_cnt += 1

                    queue.append((ny,nx))
                    






