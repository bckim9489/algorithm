import sys

t = int(input())
result = []
for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().split())
    x -= 1
    y -= 1
    i = x
    while i < m*n:
        if i%n == y:
            result.append(i+1)
            break
        i += m
    else :
        result.append(-1)
        
print(*result, sep="\n")