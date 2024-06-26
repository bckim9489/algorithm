import sys

n, m = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
ans = 0
for bitmask in range((1<<(n*m))):
    sum = 0
    for i in range(n):
        cur = 0
        for j in range(m):
            k = i*m+j
            if bitmask&(1<<k) == 0:
                cur = cur *10 + a[i][j]
            else :
                sum += cur
                cur = 0
        sum += cur
    for j in range(m):
        cur = 0
        for i in range(n):
            k = i*m+j
            if bitmask&(1<<k) !=0:
                cur = cur*10 + a[i][j]
            else :
                sum += cur
                cur = 0
        sum += cur
    ans = max(ans, sum)
print(ans)