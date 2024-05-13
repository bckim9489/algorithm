import sys

n = int(input())
d = [0 for _ in range(n+1)]

for i in range(1, n+1):
    d[i] = i
    j = 1
    while j**2 <= i:
        d[i] = min(d[i], d[i-(j**2)]+1)
        j +=1
    
print(d[n])