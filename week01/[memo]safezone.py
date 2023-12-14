'''
[NO : 2468]
* Solution Tip:
    1. BFS, DFS 둘 다 가능
    2. 주어진 숫자 중 가장 안전영역이 많은 값을 찾아야 되니 결국 다 돌아야 된다(브루트포스)
    3. bfs로 안전한 지역을 돌고 방문 기록, 시작점의 높이가 물 높이보다 낮은 곳은 아예 돌지 않고 높은 곳만 돌리는데
       그것도 방문하지 않은 곳만 bfs로 돌린다.
* Issue :
    1. [해결 전략]
        1) 미로 찾기처럼 결국 4 방향으로 BFS를 돌아야 된다는 것은 캐치함.
        2) for문으로 가장 큰값 까지 high를 돌아야 겠다는 생각은 함.
        3) 붙어있는 안전영역을 어떻게 카운트 해야할지 몰랐음
        4) 물어보니 물 높이보다 높은 곳을 BFS돌다가 낮은 곳을 만나면 BFS를 종료하고 카운트 함
        5) 결국 BFS 자체가 안전영역인 지역을 돌고 끝나면 카운트하며 방문을 기록하여 거기는 안 돌아도 되는 것이였다.
    2. [구현]
        1) 해결 전략이 세워지고는 어려운 것은 없었음
* Comment :
    여러번 BFS 돌려 같은 지점을 찾 수 있다는 점을 기억하자.
'''
import sys
sys.stdin = open("stdin", 'r')
from collections import deque

graph = []
max_high = 0
n = int(sys.stdin.readline())
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    row_max = max(row)
    
    if max_high < row_max:
        max_high = row_max

    graph.append(row)

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
result = 0

def bfs(visited, start, high):    
    queue = deque()
    queue.append(start)

    while queue:
        now_x, now_y = queue.popleft()
        if not visited[now_x][now_y]:
            visited[now_x][now_y] = True
            for i in range(4):
                nx ,ny = now_x+dx[i], now_y+dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if not visited[nx][ny] and graph[nx][ny] > high :
                        queue.append((nx, ny))

for k in range(max_high):
    cnt = 0
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > k:
                bfs(visited, (i,j), k)
                cnt += 1
    result = max(cnt, result)

print(result)
                    
