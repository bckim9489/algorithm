import sys
import heapq

sys.stdin = open('stdin', 'r')

k = int(sys.stdin.readline())

timeTable = []


for _ in range(k):
    n, st, ed = map(int, sys.stdin.readline().split())
    
    timeTable.append((n, st, ed))

timeTable.sort(key= lambda x : x[1], reverse=True)
timeTable.sort(key= lambda x : x[2], reverse=True)
print(timeTable)

