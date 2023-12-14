'''
[NO : 3190]
* Solution Tip:
    1. 뱀을 queue에 넣어야 한다.
    2. 뱀머리가 사과에 닿는지 몸에 닿는지 벽에 닿는지 확인이 필요
    3. 사과를 안 만난다면 queue에서 꺼내서 지워준다.
    4. 결국 이차원 배열을 만들어서 그래프로 접근해야한다.
* Issue :
    1. [해결 전략]
        1) 1차원의 배열로 만들다가 막혀서 2차원으로 뱀이 노다닐 보드를 만듬
        2) 시간에 따른 방향 전환을 어떻게 해야할까 하다가 시간이 가버림
        3) 풀이를 보니 시간은 계속해서 기록하고 그 시간이 딕셔너리에 있으면 회전한다
    2. [구현]
        1) while 문 안쪽부터 구현을 못했음
        2) 일단 미로찾기처럼 상하좌우를 이동할 오프셋이 필요한데 D나 L을 만나면 방향을 전환해야하기 때문에 
           시작 방향을 기준으로 반시계나 시계방향으로 오프셋을 만들어줘야 함.
        3) 뱀 자체가 그래프에 흔적을 남기도록 구현하고 흔적을 남긴 좌표를 큐에 넣어서 관리해주더라.
        4) 사과를 안만나면 꼬리를 줄여줘야하므로 큐에서 제일 처음에 넣었던 몸을 빼주고 그 좌표 값을 받아서
           그래프에 0으로 다시 돌려줘야 한다.
        4) 이동이 끝나면 방향에 관해 체크해 준다.
        5) 종료 조건은 머리가 몸통이나 벽을 만날경우 while문을 나가준다.
* Comment :
    구현이나 해결 전략을 짜는 것 자체가 틀려먹어서 더 많은 문제를 풀어봐야 할 것 같다.
'''
import sys
from collections import deque
sys.stdin = open('stdin', 'r')

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
move_list = {}
snake = deque([])

graph = [[0]*(n) for _ in range(n)]

for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    graph[x-1][y-1] = 1

l = int(sys.stdin.readline())

for _ in range(l):
    time, rotate = map(str, sys.stdin.readline().split())
    move_list[int(time)] = rotate

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] #우, 하, 좌, 상 (시계방향)
direction = 0
time = 0
head_x, head_y = 0, 0

# 몸통 : -1
# 사과 :  1
# 공간 :  0
while True:
    snake.append((head_x, head_y))
    time += 1
    
    head_x += dx[direction]
    head_y += dy[direction]

    if head_x < 0 or head_x >= n or head_y < 0 or head_y >= n or graph[head_x][head_y] == -1: # 벽꽝 or 몸꽝
        break

    if graph[head_x][head_y] != 1:
        body_x, body_y = snake.popleft()
        graph[body_x][body_y] = 0
    
    graph[head_x][head_y] = -1 # move

    if time in move_list:
        if move_list[time] == 'D':
            direction = (direction+1) % 4
        else :
            direction = (direction-1) % 4

print(time)
