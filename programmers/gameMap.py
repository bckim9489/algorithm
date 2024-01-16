'''
[고득점 kit] 게임 맵 최단거리
[memo] 
    없음
'''
from collections import deque

def solution(maps):
    answer = 0
    dx, dy = [1, -1, 0, 0],[0, 0, 1, -1]
    n, m = len(maps), len(maps[0])
    
    def bfs():
        queue = deque()
        queue.append((0,0))
        
        while queue:
            now_x, now_y = queue.popleft()
            
            for i in range(4):
                nx, ny = now_x+dx[i], now_y+dy[i]
                
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] == 1:
                        maps[nx][ny] = maps[now_x][now_y] + 1
                        queue.append((nx,ny))
                            
        return maps[n-1][m-1]
    
    answer = bfs() 
    
    if answer == 1:
        return -1
    
    return answer