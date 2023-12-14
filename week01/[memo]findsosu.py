'''
[NO : 1978]
* Solution Tip:
    1. 소수의 제곱근 판별식으로 해당 숫자의 제곱근까지의 수로 나누어 보는 것이 핵심
* Issue :
    1. [해결 전략]
        없음
    2. [구현]
        없음
* Comment :
    1. 소수의 판별에 대한 식을 해당 해당 수 까지 나눠 보는 것으로 했었지만 더 좋은 제곱근까지의 수로 판별하는 것으로 해결할 수 있다.
'''
import sys
sys.stdin = open('stdin', 'r')

n = int(sys.stdin.readline())
row = list(map(int, sys.stdin.readline().split()))
cnt = 0
for i in range(n):
    num = row[i]
    if num == 1:
        continue 

    for j in range(2, int(num**0.5)+1):
        if num%j == 0:
            break
    else :
        cnt += 1
print(cnt)