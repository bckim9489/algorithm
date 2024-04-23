import sys

k = int(input())
sign = list(map(str, sys.stdin.readline().split()))
visited = [False for _ in range(10)]

res = ["" for _ in range(k+1)]

def check(a, b, sign):
    if sign == '>' and a > b: 
        return 1
    if sign == '<' and a < b:
        return 1
    return 0

ans_min = str(sys.maxsize)
ans_max = "-1"

def selected(px, idx, singIdx):
    global ans_min
    global ans_max
    if idx == k+1:
        ans_min = min("".join(res), ans_min)
        ans_max = max("".join(res), ans_max)
        return
    
    for i in range(10):
        if visited[i]:
            continue

        if px == -1:
            visited[i] = True
            res[idx] = str(i)
            selected(i, idx+1, singIdx)
            visited[i] = False
        else:
            if check(int(res[idx-1]), i, sign[singIdx]):
                visited[i] = True
                res[idx] = str(i)
                selected(i, idx+1, singIdx+1)
                visited[i] = False

selected(-1, 0, 0)
print(ans_max)
print(ans_min)
