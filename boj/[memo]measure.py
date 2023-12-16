'''
[NO : 1037] 약수
* Solution Tip:
    N에 대한 약수 전체에 대해 가장 큰 값과 가장 작은 값의 곱은 항상 N이다.
* Issue :
    1. [해결 전략]
        없음
    2. [구현]
        없음
* Comment :
'''
import sys
sys.stdin = open('stdin', 'r')

n = input()
a = list(map(int, sys.stdin.readline().split()))

print(max(a)*min(a))
'''
a.sort()
print(a[0] * a[-1])
 '''