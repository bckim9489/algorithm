'''
[NO : 1541]
* Solution Tip:
    1. -부터 -까지 더하고 연산하면 가장 작은 값이 나옴

* Issue :
    1. [구현]
        1) 들어오는 Input에 대해 parsing 하는 부분에서 시간이 가장 많이 걸렸다.

* Comment :
    1. 해결 전략은 바로 나왔지만 Python의 문법에 아직 익숙하지 않아 시간이 걸렸으니 문법을 좀 더 알아보자.
'''
import sys
sys.stdin = open('stdin', 'r')

calc_string = sys.stdin.readline().strip().split("-")
calc_int = []

assem = sum(map(int, calc_string[0].split('+')))
for i in calc_string[1:]:
    assem -= sum(map(int, i.split('+')))

print(assem)