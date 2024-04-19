import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
a.sort()

visited = [False for _ in range(n)]
res = [0 for _ in range(m)]

def selected(idx):
    if idx == m:
        print(*res)
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        res[idx] = a[i]
        selected(idx+1)
        visited[i] = False

selected(0)