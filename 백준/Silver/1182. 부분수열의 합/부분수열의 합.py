import sys

n, s = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
ans = 0
for i in range(1, (1<<n)):
    res = 0
    for k in range(n):
        if i&(1<<k):
            res += l[k]
    if res == s:
        ans += 1

print(ans)