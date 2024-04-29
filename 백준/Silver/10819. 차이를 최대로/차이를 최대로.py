import sys
from itertools import permutations

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
ans_max = 0
perm = list(permutations(a, n))

def calc(arr):
    res_sum = 0
    for i in range(n-1):
        res_sum += abs(arr[i]-arr[i+1])
    return res_sum

for l in perm:
    arr = list(l)
    ans_max= max(ans_max, calc(arr))

print(ans_max)