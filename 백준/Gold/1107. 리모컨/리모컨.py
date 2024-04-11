import sys

n = int(input())
m = int(input())
brokenBtnList = []
minCnt = abs(n-100)

if m != 0:
    brokenBtnList = list(map(int, sys.stdin.readline().split(" ")))

for i in range(1000001):
    for j in str(i):
        if int(j) in brokenBtnList:
            break
    else:
        btnCnt = len(str(i)) + abs(i-n)
        minCnt = min(minCnt, btnCnt)

print(minCnt)