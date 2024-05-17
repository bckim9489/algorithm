import sys

n = int(input())
d=[[1, 1, 1] for _ in range(n)]

for i in range(1, n):
    d[i][0] = (sum(d[i-1]))%9901
    d[i][1] = (d[i-1][0]+d[i-1][2])%9901
    d[i][2] = (d[i-1][0]+d[i-1][1])%9901

print(sum(d[n-1])%9901)