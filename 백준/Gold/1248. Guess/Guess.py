import sys

n = int(input())
a = str(input())
graph = []
tmp = 0
cnt = 0

res = [0 for _ in range(n)]

for i in range(n, 0, -1):
    row = []
    for j in range(cnt):
        row.append("")
    for j in range(i):
        row.append(a[j+tmp])
    graph.append(row)
    tmp += i
    cnt += 1

def good(arr, idx):
    for i in range(0, idx+1):
        data = sum(arr[i:idx+1])
        if graph[i][idx] == "-":         
            if data >= 0:
                return False
        if graph[i][idx] == "+":
            if data <= 0:
                return False
        if graph[i][idx] == "0":
            if data != 0:
                return False
    return True
            

def selected(idx):
    if idx == n :
        print(*res, sep=" ")
        sys.exit()
    
    start = 0
    end = 0

    if graph[idx][idx] == "+":
        start = 1
        end = 10

    if graph[idx][idx] == "-":
        start = -10
        end = -1

    for i in range(start, end+1):
        res[idx] = i
        if idx > 0:
            if good(res, idx) == False:
                continue
        selected(idx+1)

selected(0)