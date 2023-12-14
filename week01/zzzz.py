import sys
sys.stdin = open('stdin', 'r')

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split())) + [0]


result = 0

def dfs(visited, res, idx):
    global n
    maxRes = 0

    if all(visited) == True:
        return res

    for i in range(n):
        if not visited[i]:
            nextRes = res + abs(a[idx] - a[i])
            if idx == n:
                nextRes = 0
            visited[i] = True 
            maxRes = max(maxRes, dfs(visited,nextRes, i))
            visited[i] = False
            
    return maxRes

visited = [False] * n
result = dfs(visited, 0, n)

    
print(result)