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
    

def good(idx):
    s = 0
    for i in range(idx, -1, -1):
        s += res[i]
        if graph[i][idx] == -1:         
            if s >= 0:
                return False
        if graph[i][idx] == 1:
            if s <= 0:
                return False
        if graph[i][idx] == 0:
            if s != 0:
                return False
    return True
            

def selected(idx):
    if idx == n :
        return True
    
    if graph[idx][idx] == 0:
        res[idx] = 0
        return good(idx) and selected(idx+1)

    for i in range(1, 11):
        res[idx] = i * graph[idx][idx]
        if good(idx) and selected(idx+1):
            return True
    return False

selected(0)
print(' '.join(map(str,res)))