'''
[NO : 10830]
* Solution Tip:
    1. 곱셈의 행렬버전이다.
    2. 곱셈 문제와 같이 분할 정복하되, 그 대상이 행렬이니, 행렬을 곱셈하는 함수를 만들어서 해준다
* Issue :
    1. [해결 전략]
        1) 처음부터 잘못된 접근으로 시간을 다 날려먹었다.
        2) 곱셈 문제 처럼 하면 안될 줄 알았다. 시도해볼까 하다 안했는데 그냥 해볼껄 그랬다.
    2. [구현]
        1) 전략보다 행렬 자체를 곱셈하는 것을 구현하는 것에 막혔다. 그래서 행렬 곱셈 하는 구현법을 봤다.
        2) 행렬을 곱셈하는 함수를 보고 만들고 분할 정복을 구현하여 시도했고 틀렸다.
        3) 틀린 이유는 출력에서 1000으로 나누어 주지 않아서 인데 이것도 좀 고민했다. 
            그냥 for문 두 번 쓰면 되는데 그걸 하기 싫어서 고민했다.
* Comment :
    때로는 고민하지 말고 그냥 해보자
'''
import sys
sys.stdin = open('stdin', 'r')

n, b = map(int, sys.stdin.readline().split())
matrix = []

for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    matrix.append(row)

def matrix_multi(matrix_a, matrix_b):
    global n
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += (matrix_a[i][k]*matrix_b[k][j]) % 1000
    return result

def sqr(matrix, sq):
    if sq == 1:
        return matrix
    
    result = sqr(matrix, sq//2)

    if sq % 2 == 0:
        return matrix_multi(result, result)
    else :
        return matrix_multi(matrix_multi(result, result), matrix)
        
result = sqr(matrix, b)


for a in result:
    for b in a:
        print(b %1000, end=' ')
    print('')