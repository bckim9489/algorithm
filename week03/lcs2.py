import sys
sys.stdin = open('stdin', 'r')
from collections import deque
a = [0]+list(map(str, sys.stdin.readline().strip()))
a_len = len(a)
b = [0]+list(map(str, sys.stdin.readline().strip()))
b_len = len(b)

DP = [[0]*(a_len) for _ in range(b_len)]

for i in range(1, a_len):
    for j in range(1, b_len):
        if a[i] == b[j]:
            DP[j][i] = DP[j-1][i-1] +1
        else :
            DP[j][i] = max(DP[j][i-1], DP[j-1][i])


x = b_len-1
y = a_len-1
result = deque()

while True:
    if DP[x][y] == 0:
        break

    if DP[x][y] == DP[x-1][y]:
        x -=1
        continue

    if DP[x][y] == DP[x][y-1]:
        y -=1
        continue

    result.appendleft(a[y])
    x -=1
    y -=1

print(DP[b_len-1][a_len-1])
print(*result, sep="")

    

             