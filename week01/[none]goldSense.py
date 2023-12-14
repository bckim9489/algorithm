import sys
sys.stdin = open('stdin', 'r')

sieve = [False, False, True] + [True, False] *4999
for i in range(3, int(10000**.5)+1, 2):
    if sieve[i]:
        sieve[i*i::2*i] = [False]*len(sieve[i*i::2*i])

n = int(sys.stdin.readline())

for _ in range(n):
    m = int(sys.stdin.readline())

    start = m//2

    if start == 2:
        print(start, start)
    
    if start%2 == 0:
        start -= 1
    
    for j in range(start, 0, -2):
        res = m - j
        if sieve[j] and sieve[res]:
            print(j, res)
            break