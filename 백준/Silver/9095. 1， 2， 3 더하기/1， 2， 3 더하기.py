import sys
t = int(input())

def selected2(cnt, sum, n):
    if sum > n:
        return 0
    if sum == n:
        return 1
    
    now = 0

    for i in range(1, 4):
        now += selected2(cnt+1, sum+i, n)
    
    return now

for _ in range(t):
    print(selected2(0, 0, int(input())))