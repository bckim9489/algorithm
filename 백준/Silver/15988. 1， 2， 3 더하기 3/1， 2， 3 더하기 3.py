import sys
t = int(input())
mod = 1000000009
maximum = 1000001
d = [0 for _ in range(maximum)]
d[0] = 1
for i in range(1, maximum):
    if i >= 1:
        d[i] += d[i-1]
    if i >= 2:
        d[i] += d[i-2]
    if i >= 3:
        d[i] += d[i-3]
    
    d[i] %=mod

for _ in range(t):
    n = int(input())
    print(d[n])