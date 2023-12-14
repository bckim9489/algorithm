'''
[NO : 11047]
* Solution Tip:
    일반적인 그리디 알고리즘
* Issue :
    1. [해결 전략] 
        없음
    2. [구현] 
        없음
* Comment :
    1. 구상과 구현에는 어려움이 없었으나 학습 경험에 기반해 '동전 == 그리디 or DP' 라는 느낌으로 문제를 접근했음.
        (기계적으로 반응했는데 좋은 것인가 나쁜것인가)
    2. 문제가 동전이 아니였으면 어땠을까 라는 생각을 해봄
'''
import sys
sys.stdin = open('stdin', 'r')

n, k = map(int, sys.stdin.readline().split())
wallet = []
for _ in range(n):
    wallet.append(int(sys.stdin.readline()))

wallet.sort(reverse=True)

change = k
wallect_idx = 0
cnt = 0

while change > 0:
    calc = change//wallet[wallect_idx]
    cents = int(change%wallet[wallect_idx])

    if change == cents:
        wallect_idx +=1
        continue
    
    change = cents
    cnt += calc

    wallect_idx +=1

print(cnt)
