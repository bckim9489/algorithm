import sys

n, m = map(int, sys.stdin.readline().split())
a = sorted(list(map(int, sys.stdin.readline().split())))
res = [0 for _ in range(m)]

def selected(start, idx):
    if idx == m:
        print(*res)
        return
    
    for i in range(n):
        if a[i] <= start:
            continue
        start = a[i]
        res[idx] = start
        selected(start, idx+1)

selected(0, 0)