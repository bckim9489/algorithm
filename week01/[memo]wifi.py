
'''
[NO : 2110]
* Solution Tip:
    1. 이분탐색을 해야하는 것은 최대 거리!
    2. 최소거리 ~ 최대거리를 정해서 mid 값으로 공유기를 놔둬보고 
        1) 공유기가 남으면 mid값 보다 공유기 간의 거리가 작아야 하니 mid를 end로 보고 다시 이분탐색
        2) 공유기 갯수를 넘어버리면 mid값 보다 거리를 크게 해야하니 mid+1을 start로 보고 다시 이분탐색
        3) start가 end를 넘게되면 종료
    3. 공유기를 다 놔두면 최대거리는 mid 다.
* Issue :
    1. [해결 전략]
        1) 집의 위치를 이분탐색하는 방법으로 해결 전략을 짜고 구현했으나 실패
        2) 풀이를 보니 거리 자체를 이분탐색하는 전략으로 해결해야 한다고 한다.
    2. [구현]
        1) 이분탐색 알고리즘을 잠시 까먹어서 기억을 되살리는데 시간이 좀 걸림
        2) 첫 번째 해결전략으로 실패하여 풀이의 전략으로 교체
* Comment :
    이분탐색할 대상을 잘 정해야 한다. 생각을 넒히자
'''
import sys
sys.stdin = open("stdin", 'r')

n, c = map(int, sys.stdin.readline().split())

arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

#최대거리가 어찌되오...
def binary_search(arr, start, end):
    global c
    result = 0

    while start < end:
        cnt = 1
        now_house = arr[0]; #첫집은 와이파이 무료?
     
        mid = (start + end)//2

        for idx, house in enumerate(arr):
            if mid <= house - now_house:
                cnt += 1
                now_house = house
    
        if cnt >= c:
            result = mid
            start = mid+1
        elif cnt <= c:
            end = mid

    return result

if c==2:
    print(arr[n-1] - arr[0])
else :
    print(binary_search(arr, 1, arr[-1]-arr[0]))