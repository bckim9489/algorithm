import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
d_st = [0 for _ in range(n)]
d_ed = [0 for _ in range(n)]

d_st[0], d_ed[n-1] = a[0], a[n-1]

for i in range(1, n):
    d_st[i] = a[i]
    d_st[i] = max(d_st[i], d_st[i-1] +a[i])
        
for i in range(n-2, -1, -1):
    d_ed[i] = a[i]
    d_ed[i] = max(d_ed[i], d_ed[i+1]+a[i])

ans = max(d_st)

for i in range(1, n-1):
    ans = max(ans , d_st[i-1]+d_ed[i+1])

print(ans)