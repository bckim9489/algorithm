import sys

n = int(input())
a = []
ans = 0

for i in range(n):
    t, p = map(int, sys.stdin.readline().split())
    a.append((t,p))

def selected(day, cost):
    global ans
    if day == n:
        ans = max(ans, cost)
        return
    if day > n:
        return
    
    selected(day+1, cost)
    selected(day+a[day][0], cost+a[day][1])

selected(0, 0)
print(ans)