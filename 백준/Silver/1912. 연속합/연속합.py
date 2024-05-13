import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
d = [0 for _ in range(n)]
d[0] = a[0]

for i in range(1, n):
    d[i] = max(a[i], d[i-1]+a[i])

print(max(d))