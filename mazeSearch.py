import sys
from collections import deque
sys.stdin = open('stdin', 'r')
sys.setrecursionlimit(10**9)

n, m = map(int, sys.stdin.readline().split())

maze = []

for _ in range(n):
    maze.append(list(map(int, sys.stdin.readline().strip())))

def bfs(maze, start=tuple):
    queue = deque()
    queue.append(start)

    while queue:
        x, y = queue.popleft()
        print(x, y)
        
        if 0 <= y-1 < m and maze[x][y-1] == 1:
            queue.append((x, y-1))
            maze[x][y-1] = maze[x][y] + 1

        if 0 <= y+1 < m and maze[x][y+1] == 1:
            queue.append((x, y+1))
            maze[x][y+1] = maze[x][y] + 1
            
        if 0 <= x+1 < n and maze[x+1][y] == 1:
            queue.append((x+1, y))
            maze[x+1][y] = maze[x][y] + 1

        if 0 <= x-1 < n and maze[x-1][y] == 1:
            queue.append((x-1, y))
            maze[x-1][y] = maze[x][y] + 1

    return maze[n-1][m-1]

print(bfs(maze, (0, 0)))