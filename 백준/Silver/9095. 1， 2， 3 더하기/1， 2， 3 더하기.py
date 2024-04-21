import sys
t = int(input())

def selected2(res, n):
    if res > n:
        return 0
    if res == n:
        return 1
    
    now = 0

    for i in range(1, 4):
        now += selected2(res+i, n)
    
    return now

for _ in range(t):
    print(selected2(0, int(input())))