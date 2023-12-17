'''
[NO : 2609] 최대공약수와 최소공배수
* Solution Tip:
    1. 최대공약수(GCD) 는 GCD(a, b) == GCD(b, r) 이 성립한다.
    2. 최소공배수(LCM) l은 두 수 a, b의 최대공약수 g 에 대하여 l = g * (a/g) * (b/g) 가 성립한다. 
* Issue :
    없음
* Comment :
    없음
'''
import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('stdin', 'r')
a, b = map(int, sys.stdin.readline().split())

def gcd(max_a, min_b):
    if max_a < min_b:
        max_a, min_b = min_b, max_a
    
    if min_b == 0:
        return max_a
    
    r = max_a % min_b
    #Base Case
    if r == 0:
        return min_b
    else :
        return gcd(min_b, r)


def lcm(a, b, g):
    l = g*(a//g)*(b//g)
    return l

g = gcd(a, b)
l = lcm(a, b, g)

print(g)
print(l)