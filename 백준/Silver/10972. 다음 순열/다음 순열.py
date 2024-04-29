import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

fst_idx = 0
snd_idx = 0
min_value = sys.maxsize

ans = []

if arr[0] == n and arr[-1] == 1:
    print(-1)
    sys.exit()

for i in range(n-1, 0, -1):
    if i > 0:
        if arr[i] < arr[i-1]:
            continue
        else :
            fst_idx = i - 1
            break

for i in range(fst_idx+1, n):
    if arr[fst_idx] < arr[i]:
        if arr[i] <= min_value:
            min_value = arr[i]
            snd_idx = i

arr[fst_idx], arr[snd_idx] = arr[snd_idx], arr[fst_idx]

for i in range(fst_idx+1):
    ans.append(arr[i])

for i in range(n-1, fst_idx, -1):
    ans.append(arr[i])

print(*ans, sep=" ")


