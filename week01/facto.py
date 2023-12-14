import sys
sys.stdin = open('stdin', 'r')
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())

def fact(n):
    if n <= 1:
        return 1
    
    return n*fact(n)

print(fact(n))