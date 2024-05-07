import sys
n = int(input())
p = [0]+list(map(int, sys.stdin.readline().split()))
d = [0]+[sys.maxsize]*(n)

for i in range(1, n+1):
    for j in range(1, i+1):
        d[i] = min(d[i-j]+p[j], d[i])

print(d[n])