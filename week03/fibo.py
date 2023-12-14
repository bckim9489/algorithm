import sys
sys.stdin = open('stdin', 'r')

n = int(sys.stdin.readline())
memo = {0: 0, 1:1}
tbl = {0: 0, 1:1}

#top_down(memoization)
def fibo_memo(n):
    if n < 2: return memo[n]
    if n in memo:
        return memo[n]
    
    memo[n] = fibo_memo(n-2)+fibo_memo(n-1)

    return memo[n]
print(fibo_memo(n))

#bottom-up(memoization)
def fibo_tabul(n):
    for i in range(2, n+1):
        tbl[i] = tbl[i-1]+tbl[i-2]
        
    return tbl[n]

print(fibo_tabul(n))
