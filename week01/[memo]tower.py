'''
[NO : 2468]
* Solution Tip:
    1. stack을 써서 tower의 높이가 큰 것을 계속 가지고 있고, tower가 stack에 있는 tower보다 낮다면 수신하므로 result에 기록한다.
    2. stack보다 tower가 더 높으면 stack을 pop해주고 다음 stack 탑과 비교한다.
    2. stack이 빈다면 현재 단계에서 tower보다 높은 것이 없다.
    3. 그 다음 탑을 스택에 넣고 반복한다.
       
* Issue :
    1. [해결 전략]
        1) 하나 하나 비교하는 방법으로 전략을 짜서 구현 후 도전했지만 시간초과가 났다.
        2) 높은 탑을 만날때까지 저장하는 전략으로 변경(이때까지 20분 소요)
    2. [구현]
        1) 첫 번째 실패 후 새로운 전략으로 구현하려 했으나 stack에 tower를 단일로만 이용할 생각을 하다보니 구현에 실패
        2) 풀이를 보니 tower의 높이와 index를 같이 잡아주는게 포인트(이중배열)
        3) enumerate를 쓰면 배열의 인덱스와 값을 동시에 쓸수 있다. 

* Comment :
    enumerate를 자주 써보도록 하자.
'''
import sys

sys.stdin = open('stdin', 'r')
n = int(sys.stdin.readline())
result = []
stack = []

arr = list(map(int, sys.stdin.readline().split()))

for idx, tower in enumerate(arr):
    
    while stack:
        if stack[-1][1] >= tower:
            result.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        result.append(0)
    
    stack.append((idx, tower))

print(*result)
    
    