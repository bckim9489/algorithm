import sys

n, m, k = map(int, sys.stdin.readline().split())
graph = []
visited = [[False for _ in range(m)] for _ in range(n)]
dx, dy = [1,-1,0,0],[0,0,1,-1]

for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    graph.append(row)


ans = -10001

def selected(idx, res):
    global ans
    if idx == k:
        ans = max(ans, res)
        return
    
    for x in range(n):
        for y in range(m):
            if visited[x][y]:
                continue
            
            flag = True

            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny]:
                        flag = False

            if flag:
                visited[x][y] = True
                selected(idx+1, res+graph[x][y])
                visited[x][y] = False
selected(0, 0)
print(ans)