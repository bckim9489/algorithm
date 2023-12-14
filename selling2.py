import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('stdin', 'r')
n = int(input())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [False]*n
route = []
cost_min = sys.maxsize

def dfs(start, cost):
    global cost_min
    if cost > cost_min:
        return
    if start == n:
        lastRoute = graph[route[-1]][route[0]]
        if lastRoute != 0:
            cost_min = cost_min if cost_min < cost + lastRoute else cost + lastRoute
        return
    
    for i in range(n):
        if start == 0 or (not visited[i] and graph[route[start - 1]][i] != 0):
            route.append(i)
            visited[i] = True
            dfs(start + 1, cost + graph[route[start - 1]][i])
            route.pop()
            visited[i] = False
        
dfs(0, 0) 
print(cost_min)