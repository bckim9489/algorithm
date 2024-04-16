import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())

numList = [x for x in range(1, n+1)]
ans = list(permutations(numList, m))

for idx, val in enumerate(ans):
    print(*val)