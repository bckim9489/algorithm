'''
[NO : 4375] 1
* Solution Tip:
    1. (A*B)%N = ((A%N)*(B%N))%N
    2. 분할 정복
* Issue :
    1. [해결 전략]
        1) 분할 정복 및 재귀로 나머지 연산을 하면서 값이 커지는 걸 방지하며 들어간다.
        2) 전략을 짜는 데는 문제가 없었다.
    2. [구현]
        1) 구현에서 조금 애를 먹었다. 인자 값으로 계속 result를 넘겨줘야 하는 것을 안해서 오류가 났고 30분 시간초과됨
        2) 시간 초과 이후에 인자 값으로 result를 추가해줘서 결과를 계속 들고가며 재귀를 하도록 했다.
* Comment :
    - 나머지연산은 거의 대부분 재귀로 분할정복 하는 듯...?
    - 재귀로 되면 while문으로 하는 것도 있다... 더 깔끔하고 속도가 빠르더라.
'''
import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('stdin', 'r')
#재귀 이용
ans = 0
def mod_func(n, cnt, result):

    if cnt == 1:
        return mod_func(n, cnt+1, (1%n))

    result = (result*10 +1)%n
    
    if result == 0:
        return cnt
    else :
        return mod_func(n, cnt+1, result)

while True:
    try:
        n = int(sys.stdin.readline())
        if n == 1:
            print(1)
        else :
            ans = mod_func(n, 1, 0)
            print(ans)
    except:
        break

'''
while 문 이용
while True:
    try:
        n = int(sys.stdin.readline())
    except:
        break
    num =0
    i = 1
    while True:
        num = num * 10 +1
        num %= n
        if num == 0:
            print(i)
            break
        i += 1
'''

    