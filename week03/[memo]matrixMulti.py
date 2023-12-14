'''
[NO : 11049]
* Solution Tip:
    1. 곱셈 행렬도 곱셈이기에 곱셈의 교환법칙이 성립한다.
    2. 행과 열 각각이 아닌 더 크게 행렬끼리의 곱셈으로 봐야한다.

* Issue :
    1. [해결 전략]
        1) DP를 어떻게 해야 할지 몰랐음.
        2) 주어진 입력 a, b 에 대해 집중하다보니 생각이 굳어짐(수학적으로 곱셈의 순서에 대한 특징을 떠올리지 못한 죄)
        3) 해결책은 더 크게 봐서 행렬 자체에 있었음.
        4) 연쇄행렬 최소곱셈 알고리즘의 설명 찾아봄 (행렬 곱셈의 경우의 수가 '카탈란 수'라는데 재미있다고함.)
    2. [구현]
        1) 구상한 개념을 구현하고도 틀렸는데 그 이유가 구상은 테이블에서 사선으로 타고가면서 DP를 채웠는데 난 수평으로 채우려고 해서 틀림
        2) [구현]사선으로 채울 수 있게끔 j를 반복문으로 돌린게 아니라 d라는 사선을 타고 갈 수 있는 반복문과 i를 더해 사선을 타고 갈 수 있게 함.

* Comment :
    1. 문제 해결 전략을 다양하게 구상하자.(나누고 합치고 작게보고 크게볼 필요가 있다.)
    2. 구현에 시간을 좀 더 줄이고 꼼꼼하게 디버깅하자.
'''
import sys
sys.stdin = open("stdin", "r")

n = int(sys.stdin.readline())
DP = [[0]*(n+1) for _ in range(n+1)]
P = [0]
for i in range(1, n+1):
    a, b = list(map(int, sys.stdin.readline().split()))
    if i == (n):
        P.append(a)
        P.append(b)
    else :
        P.append(a)
for d in range(1, n):
    for i in range(1, n-d+1):
        j = i+d
        if(i != j) : 
            DP[i][j] = sys.maxsize
        
        for k in range(i, j):
            DP[i][j] = min(DP[i][j], DP[i][k] + DP[k+1][j]+(P[i]*P[k+1]*P[j+1]))

print(DP[1][n])
