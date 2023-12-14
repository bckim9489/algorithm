'''
[NO : 1700]
* Solution Tip:
    1. 그리디 할 기준을 빈도 수가 아니라 최근 사용할 것을 기준으로 전략을 구상 해야한다.

* Issue :
    1. [해결 전략]
        1. 총 전자기기 리스트에서 반복되는 빈도 수를 구해서 많은 빈도인 것을 멀티탭에서 나중에 뽑으려고 했으나 틀림.
        2. 전략이 잘못됨을 느끼고 여러 방면으로 고민 했으나 전략 대상을 최근 사용할 것으로 맞추지 못함
        3. 풀이를 보고 전략 대상 변경
    2. [구현]
        1. 전략을 변경하는데 한 세월이 걸렸다. 풀이는 리스트 데이터를 그대로 유지해서 구현했지만 리스트에서 제거 되는 형식을 유지하고 싶었다.
        2. 다 구현하고 반례도 다 돌려봤지만 valueError이 떴다. 여러 방면으로 찾아봤지만 답은 없었고 멀티탭의 
            사용가능 플러그를 줄여보면서 IDE에서 에러가 뜨는 것을 확인
        3. 배열의 값으로 인덱스를 가져오는(.index())에서 없는 인덱스를 가져올 떄 런타임에러(ValueError)이 발생했다.
        3. unPlug_item_idx <= isLastest(i) 이 부분의 논리 연산자에 포함 범위에 대한 값을 잘못 구상해서 생긴 문제였다.

* Comment :
    1. 아침에 읽었던 책에서 나온 최대, 최소의 예외를 잘못 설정한 경우이다. 책에서 배운 것을 잘 써먹도록 하자.
'''
import sys
sys.stdin = open('stdin', 'r')
    
cnt = 0

n, k = map(int, sys.stdin.readline().split())

if n >= k:
    print(0)
    quit()

elec_list = list(map(int, sys.stdin.readline().split()))
p_socket = []

while True:
    if len(p_socket) == n:
        break

    if len(elec_list) == 0:
        print(0)
        quit()
    
    item = elec_list.pop(0)
    if item in p_socket:
        continue

    p_socket.append(item)

def isLastest(a):
    if a in elec_list:
        result = elec_list.index(a)
        return result
    else :
        return k

while elec_list:
    
    now_item = elec_list.pop(0)
    

    if now_item in p_socket:
        continue

    unPlug_item = 0
    unPlug_item_idx = 0
    
    for i in p_socket:
        if unPlug_item_idx <= isLastest(i):
            unPlug_item_idx = isLastest(i)
            unPlug_item = i
    
    p_socket.pop(p_socket.index(unPlug_item))
    p_socket.append(now_item)
    cnt += 1
    
print(cnt)