import sys

x = int(input())
dp = [0 for _ in range(x+1)]

# Top-down
# sys.setrecursionlimit(10**9)
# def calc(n):
#     if n == 1:
#         return 0
#     if dp[n] > 0:
#         return dp[n]
#     dp[n] = calc(n-1) +1
#     if n % 2 == 0:
#         res = calc(n//2)+1
#         dp[n] = min(dp[n], res)
#     if n % 3 == 0:
#         res = calc(n//3)+1
#         dp[n] = min(dp[n], res)
#     return dp[n]

#bottom-up
for i in range(2, x+1):
    dp[i] = dp[i-1] + 1
    if i%2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])
    if i%3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])


print(dp[x])
