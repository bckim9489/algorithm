import sys

n = int(input())
d = [0 for _ in range(n+1)]
d[0]= 1

for i in range(2, n+1, 2):
    d[i] = d[i-2]*3
    for j in range(i-4, -1, -2):
        d[i] += d[j]*2
print(d[n])