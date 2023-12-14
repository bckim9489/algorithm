import sys
sys.stdin = open('stdin', 'r')

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = {}

dx, dy = [1, 0], [0, 1]
def dfs(node):
    if node == (n-1, n-1):
        return 1
    
    if node in dp:
        return dp[node]
    
    cnt = 0
    now_y, now_x = node
    for i in range(2):
        nx, ny = now_x+dx[i]*graph[now_y][now_x], now_y+dy[i]*graph[now_y][now_x]
        if 0<= nx < n and 0<= ny < n:
            cnt += dfs((ny, nx))
                    
    dp[node] = cnt
    return cnt


print(dfs((0,0)))
print(dp)
