import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))

d_inc = [0 for _ in range(n)]
d_dec = [0 for _ in range(n)]
d = [0 for _ in range(n)]
for i in range(n):
    d_inc[i] = 1
    for j in range(i):
        if a[i] > a[j] and d_inc[i] < d_inc[j]+1:
            d_inc[i] = d_inc[j]+1

for i in range(n-1, -1, -1):
    d_dec[i] = 1
    for j in range(i, n):
        if a[i] > a[j] and d_dec[i] < d_dec[j]+1:
            d_dec[i] = d_dec[j]+1


for i in range(n):
    d[i] = d_inc[i]+d_dec[i] -1

print(max(d))