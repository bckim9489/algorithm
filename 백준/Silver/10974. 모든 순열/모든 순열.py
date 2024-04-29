import sys
from itertools import permutations

n = int(input())
numbers = [x for x in range(1, n+1)]
a = list(permutations(numbers, n))

for i in a:
    print(*i, sep=" ")