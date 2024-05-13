import sys

n, k = map(int, sys.stdin.readline().split())
d = [[0 for _ in range(n+1)] for _ in range(k+1)]
d[0][0] = 1
for i in range(1, k+1):
    for j in range(n+1):
        for l in range(j+1):
            d[i][j] += d[i-1][j-l]
            d[i][j] %= 1000000000

print(d[k][n])