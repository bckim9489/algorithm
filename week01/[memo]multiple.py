'''
[NO : 1629]
* Solution Tip:
    1. 곱셈의 규칙을 이용한다. 같은 수를 곱하면 2 제곱으로 표현이 가능하다
    2. 제곱의 규칙을 이용한다. 같은 수의 n제곱인 수와 m제곱인 수를 더하면 같은 수의
       m+n 제곱이 된다.
    3. 나누기는 결국 어디서 나눠도 같다
* Issue :
    1. [해결 전략]
        1) 예시에서 나온 값으로 (10^11) % 12 -> 
            (10 * ((10^5) * (10^5))) % 12 -> 
            (10 * ((10 * ((10^2) * (10^2))) * (10 * ((10^2) * (10^2))))) % 12
           이라는 규칙이 나옴
    2. [구현]
        1) 재귀를 어떻게 이용할 지에 대한 시간이 많이 소요됨
* Comment :
    없음
'''
import sys

a, b, c = map(int, sys.stdin.readline().split())

def multi(num, upper, mod):
    if upper ==1:
        return num%mod
    
    result = multi(num, upper//2, mod)

    if upper % 2 == 0:
        return (result*result)%mod
    else :
        return (a*result*result)%mod

print(multi(a,b,c))