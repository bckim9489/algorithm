import sys

n, m = map(int, sys.stdin.readline().split())
res = [0 for _ in range(m)]
a = [x for x in range(1, n+1)]

def selected(idx):
    if idx == m:
        print(*res)
        return

    for i in range(1, n+1):
        res[idx] = i
        selected(idx+1)

selected(0)