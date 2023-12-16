'''
[NO : 17425] 약수의 합
* Solution Tip:
    1. 약수의 반대는 배수
    2. A = BC (A의 약수 B, C) 이면 A는 B와 C의 배수이다.
* Issue :
    1. [해결 전략]
        1) DP로 해야 될 것 같아서 메모이제이션을 생각했지만 타뷸레이션으로 해결 해야 됐다.
    2. [구현]
        1) 타뷸레이션을 생각지도 못해서 망했다.
        2) 구현부를 찾아보고 다시 구현
* Comment :
    메모이제이션이나 타뷸레이션 같은 스킬을 좀 능숙하게 다뤄야겠다.
'''
import sys
sys.stdin = open('stdin', 'r')

f = [1]*1000001 #f(n)
g = [0]*1000001 #g(n)

#f(n) 타뷸레이션
for i in range(2,1000001):
    j = 1
    while i*j <=1000000:
        f[i*j] += i
        j += 1

#g(n) 타뷸레이션
for k in range(1, 1000001):
    g[k] = g[k-1]+f[k]

n = int(input())
ans = []
for _ in range(n):
    row = int(input())
    ans.append(g[row])

#print(*ans, sep='\n')
print('\n'.join(map(str, ans))+'\n')