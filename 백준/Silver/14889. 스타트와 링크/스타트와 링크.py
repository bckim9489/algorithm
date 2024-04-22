import sys

n = int(input())
a = []

for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    a.append(row)

def selected(idx, startTeam, linkTeam):    
    if idx == n:
        if len(startTeam) != n//2:
            return -1
        if len(linkTeam) != n//2:
            return -1
        
        st_cost = 0
        li_cost = 0
        for i in range(n//2):
            for j in range(n//2):
                if i == j:
                    continue
                st_cost += a[startTeam[i]][startTeam[j]]
                li_cost += a[linkTeam[i]][linkTeam[j]]
        diff = abs(st_cost-li_cost)
        return diff
    
    if len(startTeam) > n//2:
        return -1
    if len(linkTeam) > n//2:
        return -1
        
    ans = -1
    t1 = selected(idx+1, startTeam+[idx], linkTeam)
    if ans == -1 or (t1 != -1 and ans>t1):
        ans = t1

    t2 = selected(idx+1, startTeam, linkTeam+[idx])
    if ans == -1 or (t2 != -1 and ans > t2):
        ans = t2

    return ans

print(selected(0, [], []))