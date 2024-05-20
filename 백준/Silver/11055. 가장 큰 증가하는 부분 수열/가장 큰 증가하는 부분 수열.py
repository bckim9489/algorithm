import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))

d = [0 for _ in range(n)]

for i in range(n):
    d[i] = a[i]
    for j in range(i):
        if a[j] < a[i] and d[i] < d[j]+a[i]:
            d[i] = d[j]+a[i]

print(max(d))