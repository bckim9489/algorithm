import sys
sys.stdin = open('stdin', 'r')

'''
[NO : 11053]
* Solution Tip:
    다시 풀어보기
* Issue :

* Comment :
'''
n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().strip().split()))
DP = [0]*n

for i in range(n):
    DP[i] = 1
    for j in range(i):
        if num_list[i] > num_list[j]:
            DP[i] = max(DP[i], DP[j]+1)

print(max(DP))
