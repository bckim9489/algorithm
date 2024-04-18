import sys

n, m = map(int, sys.stdin.readline().split())
res = [0 for _ in range(m)]

def selected(start, idx):
    if idx == m:
        print(*res)
        return
    
    for i in range(start, n+1):
        res[idx] = i
        selected(i, idx+1)

selected(1, 0)