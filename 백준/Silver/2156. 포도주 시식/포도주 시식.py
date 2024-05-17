import sys

n = int(input())
wine = [0 for _ in range(n)]
d = [[0, 0, 0] for _ in range(n)]

for i in range(n):
    wine[i] = int(input())
    
d[0][1] = wine[0]

for i in range(1, n):
    d[i][0] = max(d[i-1][0], d[i-1][1], d[i-1][2])
    d[i][1] = d[i-1][0] + wine[i]
    d[i][2] = d[i-1][1] + wine[i]

print(max(d[n-1]))