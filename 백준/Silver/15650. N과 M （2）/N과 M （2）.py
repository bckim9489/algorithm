import sys

n, m = map(int, sys.stdin.readline().split())
res = [0 for _ in range(m)]
visited = [False for _ in range(n+1)]

def selected(start, idx):
    if idx == m:
        print(*res)
        return
    
    for i in range(start, n+1):
        if visited[i]:
            continue
        visited[i] = True
        res[idx] = i
        selected(i+1, idx+1)
        visited[i] = False

selected(1, 0)