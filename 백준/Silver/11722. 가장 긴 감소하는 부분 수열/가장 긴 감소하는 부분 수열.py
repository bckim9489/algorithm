import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))

d = [0 for _ in range(n)]

for i in range(n):
    d[i] = 1
    for j in range(i):
        if a[i] < a[j] and d[i] < d[j]+1:
            d[i] = d[j]+1

print(max(d))