import sys

n = int(input())
t = [0 for _ in range(n+2)]
p = [0 for _ in range(n+2)]
d = [-1 for _ in range(n+2)]

for i in range(1, n+1):
    t[i], p[i] = map(int, sys.stdin.readline().split())

def selected(day):
    if day == n+1:
        return 0
    if day > n+1:
        return -sys.maxsize
    if d[day] != -1:
        return d[day]
    x_res = selected(day+1)
    o_res = p[day] + selected(day+t[day])
    d[day] = max(x_res, o_res)
    return d[day]

print(selected(1))