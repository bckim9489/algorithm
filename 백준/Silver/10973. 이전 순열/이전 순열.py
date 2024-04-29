import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
ans = []
fst_idx = 0
snd_idx = 0
max_idx = -1

if a[0] == 1 and a[-1] == n:
    print(-1)
    sys.exit()

for i in range(n-1, 0, -1):
    if a[i] > a[i-1]:
        continue
    fst_idx = i-1
    break

for i in range(fst_idx+1, n):
    if a[fst_idx] > a[i]:
        if a[i] > max_idx:
            max_idx = a[i]
            snd_idx = i

a[fst_idx], a[snd_idx] = a[snd_idx], a[fst_idx]

for i in range(fst_idx+1):
    ans.append(a[i])

for i in range(n-1, fst_idx, -1):
    ans.append(a[i])

print(*ans, sep=" ")