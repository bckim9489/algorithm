'''
[NO : 8983]
* Solution Tip:
    1. 동물 위치와 사대의 거리가 문제에 나와있음을 이용(|x-a| + b)해야 함
    2. 문제에서 그 거리에 대한 값이 사정거리(L) 보다 작거나 같을 경우만 카운트 해야함
    3. 이진탐색을 할 대상은 사대의 목록에서 대상 동물의 x 좌표가 가까운 사대로 해야한다.
    4. 가까운 사대라 할지라도 오른쪽의 사대가 가까운 경우도 있으니 이진탐색으로 
        가깝다고 한 사대와 그 옆 사대 둘 다 동물과의 거리를 구한 후 가장 작은 수를 선택하여 확인한다.
* Issue :
    1. [해결 전략]
        1) 가장 먼저 y를 없애서 1차원의 이진탐색의 형태로 만드려고 함.
        2) 각 동물의 y를 l로 빼줘서(l-y) 음수인 경우는 잡지 못하고, 양수이거나 0인 경우만 생각.
        3) 하지만 각 케이스를 하기에는 시간초과가 걸릴 것이라 예상.
        4) 이진탐색의 대상을 동물로 생각하다가 풀이시간 30분을 넘겨버림
        5) 풀이를 보니 사대에 대해 특정 동물의 x값을 탐색하는 것이였음
    2. [구현]
        1) biset라이브러리를 이용해서 biset_left함수로 구현하려 했으나 특정 수에서 값이 안 맞나봄(사대가 1개인 경우는 안맞음)
        2) 그래서 그냥 이진 탐색을 직접 구현함.
* Comment :
    1. 다음에 biset를 써보자.
    2. 이진 탐색에 대한 대상을 바꿔볼 생각을 가져야 된다.
'''
import sys
sys.stdin = open('stdin', 'r')

m, n, l = map(int, sys.stdin.readline().split())

shot_place = list(map(int, sys.stdin.readline().split()))

animals = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    animals.append((x,y))

shot_place.sort()

cnt = 0

def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid - 1
    return right

for idx, animal in enumerate(animals):
    animal_x, animal_y = animal
    
    hunter = binary_search(shot_place, animal_x)
    now_hunter = abs(shot_place[hunter]-animal_x)+animal_y
    next_hunter = sys.maxsize
    if hunter < m-1:
        next_hunter = abs(shot_place[hunter+1]-animal_x)+animal_y
    
    dist = min(now_hunter, next_hunter)
    if dist <= l:
        cnt += 1

print(cnt)