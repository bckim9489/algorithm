import sys

t = int(input())
ans = [0 for _ in range(t)]
    
a = [1,2,3]

def selected(testIdx, res, n):
    if res == n:
        ans[testIdx] += 1
        return
    
    for i in range(len(a)):
        res += a[i]
        if res > n:
            break
        selected(testIdx, res, n)
        res -= a[i]

for i in range(t):
    n = int(input())
    selected(i, 0, n)

print(*ans, sep="\n")