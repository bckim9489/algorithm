import sys

n, m = map(int, sys.stdin.readline().split())
a = sorted(list(map(int, sys.stdin.readline().split())))
res = [0 for _ in range(m)]

def selected(idx):
    if idx == m:
        print(*res)
        return
    
    for i in range(n):
        res[idx] = a[i]
        selected(idx+1)

selected(0)