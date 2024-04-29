import sys
from itertools import permutations

n = int(input())
ans_min = sys.maxsize

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

history = [x for x in range(n)]

perm = list(permutations(history, n))

def calc(arr):
    global graph
    global n
    res_sum = 0
    for i in range(n):
        
        if i != n-1 and graph[arr[i]][arr[i+1]] != 0:
            res_sum += graph[arr[i]][arr[i+1]]
        elif i == n-1 and graph[arr[i]][arr[0]] != 0:
            res_sum += graph[arr[i]][arr[0]]
        else : 
            res_sum = sys.maxsize
            break

    return res_sum

for tp in perm:
    arr = list(tp)
    ans_min = min(ans_min, calc(arr))

print(ans_min)
        