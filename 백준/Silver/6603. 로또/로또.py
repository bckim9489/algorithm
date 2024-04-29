import sys

res = [0 for _ in range(6)]

def selected(arr, idx, visited, px):
    if idx == 6:
        print(*res, sep=" ")
        return
    
    for i in range(px, len(arr)):
        if visited[i]:
            continue
        
        visited[i] = True
        res[idx] = arr[i]
        selected(arr, idx+1, visited, i)
        visited[i] = False

while True:
    s = list(map(int, sys.stdin.readline().split()))
    k = s[0]
    if k == 0:
        break
    s.pop(0)
    visited = [False for _ in range(k)]
    s.sort()

    selected(s, 0, visited, 0)
    print("")

