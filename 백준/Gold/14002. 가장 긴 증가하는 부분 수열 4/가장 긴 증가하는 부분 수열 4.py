import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
d = [1 for _ in range(n)]
v = [-1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            if d[i] < d[j]+1:
                d[i] = d[j]+1
                v[i] = j
ans = 0
max_idx = 0
for idx, value in enumerate(d):
    if ans < value:
        ans = value
        max_idx = idx

p = max_idx

def traceback(p):
    if p == -1:
        return
    traceback(v[p])
    print(a[p], end=" ")

print(ans)
traceback(p)