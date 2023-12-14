'''
[NO : 2470]
* Solution Tip:
    1. 용액들을 정렬해서 첫 인덱스와 마지막 인덱스에 포인터를 두는 듯한 변수를 둔다.
    2. 두 용액을 더해 절대값을 min으로 두면서 
        1) 더한 실제값이 0 보다 크면 마지막 인덱스를 찍고 있는 포인터를 감소시키고
        2) 더한 실제값이 0 보다 작으면 처음 인덱스를 찍고 있는 포인터를 증가시킨다.
    3. 위 과정을 통해 0과 가장 가까운 범위를 탐색하고 포인터가 교차되면 두 값을 리턴한다.
* Issue :
    1. [해결 전략]
        1) 조합으로 해결 전략을 짜고 했으나 메모리 초과
        2) 스터디 동료에게 투 포인터라는 해결 전략으로 마치 퀵 정렬을 하듯 줄이는 전략을 듣고 구현을 시도함
    2. [구현]
        1) 구현을 다 하고 계속 틀렸다고 나오길래 고민을 했다. 알고보니 출력문제였다(괄호가 같이 출력되서 문제)
* Comment :
    투 포인터를 배웠다!
'''
import sys
sys.stdin = open('stdin', 'r')

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

def two_pointer():
    global n
    a_idx = 0
    b_idx = 0
    pointer_1 = 0
    pointer_2 = n-1
    min_val = sys.maxsize
    while pointer_1 < pointer_2:
        calc = arr[pointer_1] + arr[pointer_2]
        if min_val > abs(calc):
            min_val = abs(calc)
            a_idx = pointer_1
            b_idx = pointer_2
        
        if  calc != 0:
            if 0 > calc:
                pointer_1+=1
            else :
                pointer_2-=1
                
        if calc == 0: 
            break

    return arr[a_idx], arr[b_idx]

print(*two_pointer())