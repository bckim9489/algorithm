'''
다시보기
'''
import sys
sys.stdin = open('stdin', 'r')

n, m = map(int, sys.stdin.readline().split())
small_stone = []
DP = [[10001]* (int((2*n)**0.5)+2)  for _ in range(n+1)]

for _ in range(m):
    stone = int(sys.stdin.readline())
    small_stone.append(stone)

DP[1][0] = 0
for i in range(2, n+1):
    if i in small_stone:
        continue
    for j in range(1, int((2*i)**0.5)+1):
        DP[i][j] = min(DP[i-j][j-1], DP[i-j][j],DP[i-j][j+1]) +1

result = min(DP[n])

if result == 10001:
    print(-1)
else :
    print(result)