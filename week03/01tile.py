import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('stdin', 'r')

n = int(sys.stdin.readline())
memo = {1 : 1, 2 : 2}

for i in range(3, n+1):
    memo[i] = (memo[i-1]+memo[i-2])%15746

print(memo)
print(memo[n])