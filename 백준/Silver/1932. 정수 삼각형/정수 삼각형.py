import sys

n = int(input())
d = [[0]*n for _ in range(n)]
tri = []

for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    tri.append(row)

d[0][0] = tri[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j > 0:
            d[i][j] = max(d[i-1][j], d[i-1][j-1]) +tri[i][j]
        else :
            d[i][j] = d[i-1][j] + tri[i][j]

print(max(d[n-1]))