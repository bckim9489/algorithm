import sys

n = int(input())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = sys.maxsize
for i in range((1<<n)):
    cnt = 0

    for j in range(n):
        if i&(1<<j) != 0:
            cnt += 1
    if cnt != n//2:
        continue

    start_team, link_team = [], []
    start_sum, link_sum = 0, 0

    for j in range(n):
        if i&(1<<j) != 0:
            start_team.append(j)
        else :
            link_team.append(j)
    
    if len(start_team) != n//2:
        continue

    for j in range(n//2):
        for k in range(n//2):
            if j == k:
                continue
            start_sum += graph[start_team[j]][start_team[k]]
            link_sum += graph[link_team[j]][link_team[k]]
    
    ans = min(ans, abs(start_sum-link_sum))

print(ans)

