import sys

n = int(input())
a = str(input())
graph = [[0 for _ in range(n)] for _ in range(n)]

res = [0 for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(i,n):
        if a[cnt] == '0':
            graph[i][j] = 0
        elif a[cnt] == '+':
            graph[i][j] = 1
        else:
            graph[i][j] = -1
        cnt += 1
    

def good(arr, idx):
    for i in range(0, idx+1):
        data = sum(arr[i:idx+1])
        if graph[i][idx] == -1:         
            if data >= 0:
                return False
        if graph[i][idx] == 1:
            if data <= 0:
                return False
        if graph[i][idx] == 0:
            if data != 0:
                return False
    return True
            

def selected(idx):
    if idx == n :
        print(*res, sep=" ")
        sys.exit()
    
    start = 0
    end = 0

    if graph[idx][idx] == 1:
        start = 1
        end = 10

    if graph[idx][idx] == -1:
        start = -10
        end = -1
    
    if graph[idx][idx] == 0:
        res[idx] = 0
        selected(idx+1)
    else :
        for i in range(start, end+1):
            res[idx] = i
            if idx > 0:
                if good(res, idx) == False:
                    continue
            selected(idx+1)

selected(0)