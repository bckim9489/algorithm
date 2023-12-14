import sys
from itertools import combinations
input = list(map(int, sys.stdin.readline().rstrip().split())) # n개수 s
n = list(map(int, sys.stdin.readline().rstrip().split())) # 정수 n
cnt = 0

# 부분 수열 구하기 -> 조합. 1/2/3/4/5개 뽑을 때 s
for i in range(1, len(n) + 1):  # 1부터 시작하니까 공집합 고려 X
    data = list(combinations(n, i))    # 요소 1~5개인 조합 뽑음

    for j in data:
        if sum(j) == input[1]:
            cnt += 1
print(cnt)