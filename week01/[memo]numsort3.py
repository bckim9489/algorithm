'''
[NO : 10989]
* Solution Tip:
    1. 주어진 메모리 제한이 8mb이고 입력으로 줄 수 있는 수의 갯수는 
        10,000,000(천만)개인데 int가 4byte라고 하면 40mb가 필요해서 다 못 담는다.
    2. 그리고 수의 크기는 10,000보다 작다고 한다. 
    3. 1부터 10,000 까지 수를 다 담아도 30kb이니 가능하다.
    4. 도수 정렬을 이용해야 한다.
* Issue :
    1. [해결 전략]
        1) 정렬 문제니 당연히 공간복잡도에 영향이 없는 것을 쓰려고 여러 정렬 알고리즘을 써보다가 실패
        2) 같은 스터디원의 설명을 들으니 10001개의 배열공간을 만들어 수를 다 넣고 배열의 값으로 카운트를 넣었다고 한다.
        3) 그게 도수 정렬....
    2. [구현]
        1) 구현은 어렵지 않았다.
* Comment :
    매번 적는 것이지만 생각을 확장하자
'''
import sys
sys.stdin = open('stdin', 'r')

n = int(sys.stdin.readline())
arr = [0]*10001

for i in range(n):
    row = int(sys.stdin.readline())
    arr[row] +=1

for i in range(10001):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)