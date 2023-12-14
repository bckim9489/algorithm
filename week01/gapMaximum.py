import sys
sys.stdin = open('stdin', 'r')

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

result = 0

def dfs(visited, res, idx, cnt):
    global n
    maxRes = 0

    if cnt == n-1:
        return res

    for i in range(n):
        if not visited[i]:
            nextRes = res + abs(a[idx] - a[i])
            visited[i] = True 
            maxRes = max(maxRes, dfs(visited,nextRes, i, cnt+1))
            visited[i] = False
            
    return maxRes

for i in range(n):
    visited = [False] * n
    visited[i] = True
    result = dfs(visited, 0, i, 0)
    
print(result)