'''
[NO : 1931]
* Solution Tip:
    1. 기준은 종료시간이다. 그럼 회의를 많이 우겨 넣을 수 있다.
    2. 시작 시간으로 정렬 후, 끝나는 시간으로 정렬 해주어야 한다.(시작과 동시에 종료되는 경우가 있어서 그럼)
    3. For문을 두 번 써서 DP처럼 풀면 시간초과 남
    
* Issue :
    1. [해결 전략]
        1) 시작 시간으로 정렬 후, 시작시간이 빠른 순으로 종료 시간을 물면서 내려갔지만 시작시간이 빠르다고 해서 많은 회의를 할 수 있는 것은 아니였다.
        2) 그래서 각 회의의 시작시간을 기준으로 For문을 한번 더 돌리면서 기록했는데 결국 시간초과 됨
        3) 고민을 하다 시간이 넘어가서 풀이를 봄
        4) 해답은 종료시간을 기준으로 하되, 시작과 동시에 종료되는 경우(시작시간 == 종료시간)가 있기에 시작시간으로 먼저 정렬해준 뒤 한다.
        5) 그렇게 되면 종료시간을 기준으로 종료시간이 같으면 시작시간이 빠른 회의가 앞으로 나오고 꼬리를 물면서 들어가면 For문 하나로 구현된다.

    2. [구현]
        1) 리스트를 정렬할 때, 'list.sort(key = lambda x : x[0])'를 써야하는데 고민했다.

* Comment :
    1. For문을 꼭 중첩해서 비교하는 것에 너무 꽂혀있었다. 더 넒게 생각할 필요가 있다. 
        시간초과가 났다면 중첩 반복문이 O(n^2) 이니까 안먹힌다는 건데 너무 꽂혀 있었다.
'''
import sys
sys.stdin = open('stdin', 'r')

n = int(sys.stdin.readline())

sche = []
cnt= 1

for _ in range(n):
    start_time, end_time = map(int, sys.stdin.readline().split())
    sche.append((start_time, end_time))

sche.sort(key= lambda x: x[0])
sche.sort(key= lambda x: x[1])

first_end = sche[0][1]
for next_start, next_end in sche[1:]:
    if first_end <= next_start:
        cnt +=1
        first_end = next_end

print(cnt)