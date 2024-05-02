import sys
from itertools import combinations

n, s = map(int, sys.stdin.readline().split())
input_arr = list(map(int, sys.stdin.readline().split()))

cnt = 0

def foo(n):
    global cnt
    for i in range(1,n+1):
        a = combinations(input_arr,i)
        for j in a:
            b = list(j)
            if sum(b) == s:
                cnt += 1    
    print(cnt)

foo(n)