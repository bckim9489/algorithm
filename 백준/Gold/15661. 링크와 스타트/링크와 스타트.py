import sys

n = int(input())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def selected(idx, s, l):
    if idx == n:
        t1 = 0
        t2 = 0
        for i in range(len(s)):
            for j in range(len(s)):
                if i == j:
                    continue
                t1 += a[s[i]][s[j]]
        for i in range(len(l)):
            for j in range(len(l)):
                if i == j:
                    continue
                t2 += a[l[i]][l[j]]
        
        return abs(t1-t2)
    
    ans = -1
    t1 = selected(idx+1, s+[idx], l)
    if ans == -1 or ans > t1:
        ans = t1
    t2 = selected(idx+1, s, l+[idx])
    if ans == -1 or ans > t2:
        ans = t2
    
    return ans

print(selected(0, [], []))