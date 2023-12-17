import sys
sys.stdin = open('stdin', 'r')
MAX = 10000
# 간단 명료하게 에라토스테네스의 체 만들기
sieve = [False, False, True] + [True, False] *4999
        #  0  ,  1   ,   2      홀수,  짝수  각각 4999개(1,2 와 합치면 10000개)

for i in range(3, int(MAX**.5)+1, 2): #3의 배수부터 홀수 개씩 확인.
    if sieve[i]:
        #자기 자신을 제외한 i배수를 모두 false로 바꿈
        sieve[i*i::2*i] = [False]*len(sieve[i*i::2*i])


n = int(sys.stdin.readline())

for _ in range(n):
    m = int(sys.stdin.readline())

    start = m//2

    if start == 2:
        print(start, start)
    
    if start%2 == 0:
        start -= 1
    
    for j in range(start, 0, -2):
        res = m - j
        if sieve[j] and sieve[res]:
            print(j, res)
            break