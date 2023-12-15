'''
[NO : 0000]
* Solution Tip:

* Issue :
    1. [해결 전략]

    2. [구현]

* Comment :

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

    