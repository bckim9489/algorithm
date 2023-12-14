'''
[NO : 2630]
* Solution Tip:
    1. 쿼드 트리 문제라고 함
    2. 분할 정복으로 풀어야 됨
    3. 전체를 4분할 해서 재귀로 작은 사각형을 또 4분할 해서 탐색
* Issue :
    1. [해결 전략]
        1) 분할 전략은 이해 했으나 사분면을 어떻게 찾아야 될지 고민했음
        2) 사실 문제에 n/2라고 나와있었음, 보고 전략 구상함
    2. [구현]
        1) for문에서 막힘, n개 만큼 for문이 돌아야하는데 각 사분면은 재귀를 돌 수록 n/2가 되서 고민함
        2) 사실 시작점도 0에서 계속 시작하는게 아니였음, 시작점이 바뀌고 n도 바뀜, 
           (ex. n = 8, start = 0 -> 다음 재귀 시, n = 4, start 0 -> 1사분면,
            다 돌고 다음 재귀 n=4, start = 4 -> for 문에서 n+start라서 4~8까지 돔)
* Comment :
    쿼드트리 문제 풀어보기
'''
import sys
sys.stdin = open("stdin", 'r')

n = int(sys.stdin.readline())

graph = []

for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    graph.append(row)

blue_cnt = 0
white_cnt = 0

def divide(start_x, start_y, n):
    global blue_cnt, white_cnt
    color = graph[start_x][start_y]

    for i in range(start_x, n+start_x):
        for j in range(start_y, n+start_y):
            if color != graph[i][j]:
                divide(start_x, start_y, n//2)           #1사분면
                divide(start_x+n//2, start_y, n//2)      #2사분면
                divide(start_x, start_y+n//2, n//2)      #3사분면
                divide(start_x+n//2, start_y+n//2, n//2) #4사분면
                return

    if color == 0:
        white_cnt += 1
    else :
        blue_cnt += 1

divide(0,0,n)

print(white_cnt)
print(blue_cnt)