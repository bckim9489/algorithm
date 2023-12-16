'''
[NO : 17427] 약수의 합 2
* Solution Tip:
    약수의 반대는 배수다.
    N의 배수는 모두 N을 약수로 갖는 수.
    N이하의 자연수 중에 i을 약수로 갖는 수(=i의 배수)의 갯수는 N//i 개
    f(n) = (n//1) * 1 + (n//2) *2 + ...(n//n)*n
* Issue :
    1. [해결 전략]
        없음
    2. [구현]
        없음
* Comment :
'''
import sys
sys.stdin = open('stdin', 'r')

n = int(input())
result = 0
for i in range(n):
    result += (n//(i+1))*(i+1)

print(result)