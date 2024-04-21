import sys

l, c = map(int, sys.stdin.readline().split())
a = list(map(str, sys.stdin.readline().split()))
a.sort()

res = ["" for _ in range(l)]

def selected(px, idx):
    if idx == l:
        chk = ["a", "e", "i", "o", "u"]
        cnt_chk = 0
        cnt_else = 0
        
        for _, value in enumerate(res):
            if value in chk:
                cnt_chk += 1
            else :
                cnt_else += 1

        if cnt_chk > 0 and cnt_else > 1:
            print(*res, sep="")
        return
    
    for i in range(px, c):
        res[idx] = a[i]
        selected(i+1, idx+1)

selected(0, 0)