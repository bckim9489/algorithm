import sys

n = int(input())
d = [[0]*10 for _ in range(n+1)]
ans = 0
for i in range(1, 10):
    d[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j >= 1:
            d[i][j] += d[i-1][j-1]    
        if j <= 8:
            d[i][j] += d[i-1][j+1]
        
        d[i][j] %= 1000000000

print(sum(d[n])%1000000000)